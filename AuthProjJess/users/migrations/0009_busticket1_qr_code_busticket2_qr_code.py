# Generated by Django 4.2 on 2024-01-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_busticket2_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='busticket1',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
        migrations.AddField(
            model_name='busticket2',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
    ]