# Generated by Django 2.2.6 on 2020-05-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('civam', '0003_auto_20200528_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personorinstitute',
            old_name='private_catalog_date',
            new_name='dates',
        ),
    ]
