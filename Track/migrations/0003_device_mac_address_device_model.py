# Generated by Django 4.2.3 on 2023-07-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Track', '0002_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='MAC_Address',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
    ]