# Generated by Django 2.2.6 on 2020-05-25 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('civam', '0003_item_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location_of_originals',
            field=models.ManyToManyField(blank=True, related_name='locations', to='civam.PersonOrInstitute'),
        ),
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ManyToManyField(blank=True, related_name='item_creators', to='civam.PersonOrInstitute'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='place_created',
        ),
        migrations.AddField(
            model_name='item',
            name='place_created',
            field=models.ManyToManyField(blank=True, related_name='places_created', to='civam.PersonOrInstitute'),
        ),
        migrations.CreateModel(
            name='Narrative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='narratives_created', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='narratives', to='civam.Item')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='narrative_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'narratives',
            },
        ),
    ]
