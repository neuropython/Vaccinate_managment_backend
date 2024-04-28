# Generated by Django 5.0.2 on 2024-04-06 14:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinateapp', '0007_alter_vaccine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservaccine',
            name='fist_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='uservaccine',
            name='vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine', to='vaccinateapp.vaccine'),
        ),
    ]