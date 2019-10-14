# Generated by Django 2.2.6 on 2019-10-14 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civam', '0005_auto_20191014_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
