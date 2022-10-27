# Generated by Django 4.0.5 on 2022-10-26 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_boltfleet_uberfleet_uklonfleet_alter_fleet_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_status', models.CharField(max_length=35)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fleet')),
            ],
        ),
    ]
