from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, opiskelijanumero, email, etunimi, sukunimi, password, is_aktiivinen=True, is_staff=False, is_admin=False):
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

    def create_staffuser(self, opiskelijanumero, email, etunimi, sukunimi, password):
        user = self.create_user(
            opiskelijanumero,
            email,
            etunimi,
            sukunimi,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, opiskelijanumero, email, etunimi, sukunimi, password):
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
        return f"{self.etunimi} {self.sukunimi} ({self.opiskelijanumero})"