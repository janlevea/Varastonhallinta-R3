# Generated by Django 4.0.3 on 2022-04-26 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('varasto', '0002_alter_varastotapahtuma_palautuspaiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuote',
            name='maara',
            field=models.IntegerField(default=1, verbose_name='Määrä'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='varastotapahtuma',
            name='arkistotunnus',
            field=models.CharField(default=uuid.UUID('c438b69c-c538-11ec-99b1-d037456acbfc'), editable=False, max_length=37, unique=True, verbose_name='Arkistotunnus'),
        ),
        migrations.AlterField(
            model_name='varastotapahtuma',
            name='palautuspaiva',
            field=models.DateField(default=datetime.datetime(2022, 5, 10, 8, 13, 34, 253495, tzinfo=utc), verbose_name='Palautuspäivä'),
        ),
    ]
