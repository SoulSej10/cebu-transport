# Generated by Django 4.2 on 2023-12-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_request_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_name', models.CharField(max_length=255)),
                ('destination_name', models.CharField(max_length=255)),
                ('distance', models.FloatField()),
                ('fee', models.FloatField()),
                ('fee_per_km_beyond_distance', models.FloatField(default=0)),
            ],
            options={
                'unique_together': {('origin_name', 'destination_name')},
            },
        ),
    ]
