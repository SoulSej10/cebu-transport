# Generated by Django 4.2 on 2023-12-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_busticket2_delete_busticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busticket2',
            name='discount',
            field=models.CharField(choices=[('student', 'Student (20% discount)'), ('senior_citizen', 'Senior Citizen'), ('voucher', 'Voucher'), ('regular', 'Regular')], default='none', max_length=15),
        ),
    ]
