# Generated by Django 5.0.4 on 2024-05-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0021_alter_employee_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
