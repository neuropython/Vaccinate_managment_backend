# Generated by Django 5.0.2 on 2024-03-08 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinateapp', '0003_vaccine_period'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='period',
            field=models.CharField(choices=[('MO', 'month'), ('YR', 'year'), ('DT', 'day'), ('NL', 'null')], default='MO', max_length=2),
        ),
        migrations.CreateModel(
            name='UserVaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=100)),
                ('dose', models.IntegerField(default=1)),
                ('next_date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccinateapp.vaccine')),
            ],
        ),
    ]
