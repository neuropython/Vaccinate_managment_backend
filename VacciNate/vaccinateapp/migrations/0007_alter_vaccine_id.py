# Generated by Django 5.0.2 on 2024-04-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinateapp', '0006_rename_next_date_uservaccine_fist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]