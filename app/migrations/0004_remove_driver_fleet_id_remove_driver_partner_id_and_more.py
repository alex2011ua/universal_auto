# Generated by Django 4.0.5 on 2022-10-31 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_client_user_id_remove_driver_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='fleet_id',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='partner_id',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='vehicle_id',
        ),
        migrations.AddField(
            model_name='driver',
            name='fleet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.fleet'),
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.vehicle'),
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
    ]
