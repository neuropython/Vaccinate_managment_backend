# Generated by Django 5.0.2 on 2024-04-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinateapp', '0008_alter_uservaccine_fist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='status',
            field=models.CharField(choices=[('done', 'done'), ('pending', 'pending'), ('cancelled', 'cancelled')], default='pending', max_length=10),
        ),
    ]
