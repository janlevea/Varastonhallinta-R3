from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# from django.utils.translation import gettext_lazy as _

# Importoi date/time-kirjastot käytettäväksi aikaleimoissa/palautuspäivässä
from datetime import timedelta
from django.utils import timezone

# UUID arkistotunnuksen luontia varten
import uuid

class UserManager(BaseUserManager):
    def create_user(self, opiskelijanumero, email, etunimi, sukunimi, password=None, is_aktiivinen=True, is_staff=False, is_admin=False):
        if not opiskelijanumero:
            raise ValueError("Käyttäjällä täytyy olla opiskelijanumero")
        if not email:
            raise ValueError("Käyttäjällä täytyy olla sähköpostiosoite")
        if not password:
            raise ValueError("Käyttäjällä täytyy olla salasana")
        if not etunimi:
            raise ValueError("Käyttäjällä täytyy olla etunimi")
        if not sukunimi:
            raise ValueError("Käyttäjällä täytyy olla sukunimi")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.opiskelijanumero = opiskelijanumero
        user_obj.etunimi = etunimi
        user_obj.sukunimi = sukunimi
        user_obj.set_password(password) # aseta salasana
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.aktiivinen = is_aktiivinen
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, opiskelijanumero, email, etunimi, sukunimi, password=None):
        user = self.create_user(
            opiskelijanumero,
            email,
            etunimi,
            sukunimi,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, opiskelijanumero, email, etunimi, sukunimi, password=None):
        user = self.create_user(
            opiskelijanumero,
            email,
            etunimi,
            sukunimi,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class Kayttaja(AbstractBaseUser):
    opiskelijanumero = models.CharField(unique=True,
        max_length=5, null=False, verbose_name="Opiskelijanumero")

    etunimi = models.CharField(max_length=64)
    sukunimi = models.CharField(max_length=64)
    email = models.EmailField(max_length=200, unique=True, verbose_name="Sähköposti")
    aktiivinen = models.BooleanField(default=True, verbose_name="Aktiivinen") # voi kirjautua
    staff = models.BooleanField(default=False, verbose_name="Henkilökunta") # staff, not superuser
    admin = models.BooleanField(default=False, verbose_name="Admin") # superuser
    liittynyt = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "opiskelijanumero"
    REQUIRED_FIELDS = ["email", "etunimi", "sukunimi"]

    objects = UserManager()

    def get_kokonimi(self):
        return f"{self.etunimi} {self.sukunimi}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_aktiivinen(self):
        return self.aktiivinen

    class Meta:
        verbose_name = "Käyttäjä"
        verbose_name_plural = "Käyttäjät"
    def __str__(self):
        return f"{self.opiskelijanumero}"

'''
# Onko tämä tarpeellinen???
class Varasto(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    varastotyyppi = models.CharField(max_length=30, null=False, verbose_name="Varastotyyppi")
    nimi = models.CharField(max_length=30, null=False, verbose_name="Nimi")
    class Meta:
        verbose_name = "Varasto"
        verbose_name_plural = "Varastot"
    def __str__(self):
        return f"ID: {self.id}, Tyyppi: {self.varastotyyppi}, Nimi: {self.nimi}"
'''

class Tuoteryhma(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nimi = models.CharField(max_length=50, null=False, verbose_name="Nimi")
    class Meta:
        verbose_name = "Tuoteryhmä"
        verbose_name_plural = "Tuoteryhmät"
    def __str__(self):
        return f"id({self.id}) {self.nimi}"

class Tuote(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    viivakoodi = models.CharField(max_length=30, null=False, verbose_name="Viivakoodi")
    tuoteryhma = models.ForeignKey(Tuoteryhma, null=False, on_delete=models.PROTECT, verbose_name="Tuoteryhmä")
    nimike = models.CharField(max_length=50, null=False, verbose_name="Nimike")
    hankintapaikka = models.CharField(max_length=50, null=False, verbose_name="Hankintapaikka")
    kustannuspaikka = models.CharField(max_length=10, null=False, verbose_name="Kustannuspaikka")
    tuotekuva = models.BinaryField(null=False, verbose_name="Tuotekuva")
    class Meta:
        verbose_name = "Tuote"
        verbose_name_plural = "Tuotteet"
    def __str__(self):
        return f"id({self.id}) {self.tuoteryhma.nimi}/{self.nimike}"

class Varastotapahtuma(models.Model):   
    id = models.AutoField(primary_key=True, null=False)
    arkistotunnus = models.CharField(
        default=uuid.uuid1(), editable=False, max_length=37, null=False, blank=False, unique=True, verbose_name="Arkistotunnus")

    #varasto = models.ForeignKey(
    #    Varasto, null=False, on_delete=models.PROTECT, verbose_name="Varasto")
    tuote = models.ForeignKey(
        Tuote, null=False, on_delete=models.PROTECT, verbose_name="Tuote")
    maara = models.IntegerField(null=False, verbose_name="Määrä")
    aikaleima = models.DateTimeField(auto_now_add=True,
        null=False, editable=False, verbose_name="Aikaleima")
    palautuspaiva = models.DateField(
        null=False, default=(timezone.now() + timedelta(days=14)), verbose_name="Palautuspäivä")
    asiakas = models.ForeignKey(
        Kayttaja, null=False, related_name="asiakas", on_delete=models.PROTECT, verbose_name="Asiakas")
    varastonhoitaja = models.ForeignKey(
        Kayttaja, null=False, related_name="varastonhoitaja", on_delete=models.PROTECT, verbose_name="Varastonhoitaja")
    class Meta:
        verbose_name = "Varastotapahtuma"
        verbose_name_plural = "Varastotapahtumat"
    def __str__(self):
        return f"id({self.id}) {self.tuote.nimike} {self.maara}kpl, Asiakas: {self.asiakas}, Varastonhoitaja: {self.varastonhoitaja}"