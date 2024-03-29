# Generated by Django 3.2.5 on 2021-07-23 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DelieveryPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('bike', 'bike'), ('scooter', 'scooter'), ('truck', 'truck')], max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.IntegerField(choices=[(1, '6-9'), (2, '9-13'), (3, '16-19'), (4, '19-23')])),
                ('date', models.DateField(auto_now_add=True)),
                ('order_id', models.IntegerField()),
                ('delievery_partner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='slot_finder.delieverypartner')),
            ],
        ),
        migrations.AddField(
            model_name='delieverypartner',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='slot_finder.vehicle'),
        ),
    ]
