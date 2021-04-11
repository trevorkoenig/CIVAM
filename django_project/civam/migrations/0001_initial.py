# Generated by Django 3.1.7 on 2021-04-10 23:48

import civam.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('dates', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/')),
                ('public', models.BooleanField(default=True)),
                ('provenance', models.TextField(blank=True, null=True)),
                ('citation', models.TextField(blank=True, null=True)),
                ('historical_note', models.TextField(blank=True, null=True, verbose_name='Historical/Biographical Note')),
                ('access_notes_or_rights_and_reproduction', models.TextField(blank=True, null=True)),
                ('geographical_location', models.CharField(blank=True, max_length=511, null=True)),
                ('private_notes', models.TextField(blank=True, null=True)),
                ('private_cataloger', models.CharField(blank=True, max_length=511, null=True)),
                ('private_catalog_date', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Heritage Item')),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/items/')),
                ('description', models.TextField(blank=True)),
                ('culture_or_community', models.CharField(blank=True, max_length=127, null=True)),
                ('other_forms', models.TextField(blank=True, null=True)),
                ('digital_heritage_item', models.CharField(blank=True, max_length=127, null=True)),
                ('date_of_creation', models.CharField(blank=True, max_length=127, null=True)),
                ('physical_details', models.TextField(blank=True, null=True)),
                ('access_notes_or_rights_and_reproduction', models.TextField(blank=True, null=True)),
                ('catalog_number', models.CharField(blank=True, max_length=31, null=True)),
                ('external_link', models.URLField(blank=True, null=True)),
                ('provenance', models.TextField(blank=True, null=True)),
                ('private_notes', models.TextField(blank=True, null=True)),
                ('citation', models.TextField(blank=True, null=True)),
                ('historical_note', models.TextField(blank=True, max_length=255, null=True, verbose_name='Historical/Biographical Note')),
                ('place_created', models.CharField(blank=True, max_length=511, null=True)),
                ('private_cataloger', models.CharField(blank=True, max_length=511, null=True)),
                ('private_catalog_date', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='civam.collection')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('location', models.CharField(choices=[('ABOUT', 'About Headline'), ('MISSION', 'About: Our Mission'), ('ORIGINS', 'About: Origins'), ('PEOPLE1', 'About: People: Bio 1'), ('PEOPLE2', 'About: People: Bio 2'), ('PEOPLE3', 'About: People: Bio 3'), ('PEOPLE4', 'About: People: Bio 4'), ('CONTACT', 'About: Resources & Contact Information')], default='ABOUT', max_length=8, unique=True, verbose_name='Location of text on site')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='civam.item')),
            ],
        ),
        migrations.CreateModel(
            name='PersonOrInstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125)),
                ('culture', models.CharField(blank=True, max_length=255, null=True)),
                ('dates', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('historical_note', models.TextField(blank=True, null=True)),
                ('isPerson', models.BooleanField()),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/pori/')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('private_notes', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PorI_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Pori_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person or Institution',
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_article_tag_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_article_tag_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Lower('word')],
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/articles/', verbose_name='Cover Image')),
                ('publish_on', models.DateTimeField(verbose_name='When to publish the article')),
                ('content', models.TextField(verbose_name='Article Text')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_article_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_article_modified', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='news_article_tag', to='civam.NewsTag')),
            ],
            options={
                'ordering': ['publish_on'],
            },
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
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='narratives', to='civam.item')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='narrative_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'narratives',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='keyword_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='keyword_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Lower('word')],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='creator',
            field=models.ManyToManyField(blank=True, related_name='item_creators', to='civam.PersonOrInstitute'),
        ),
        migrations.AddField(
            model_name='item',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='item_keywords', to='civam.Keyword'),
        ),
        migrations.AddField(
            model_name='item',
            name='location_of_originals',
            field=models.ManyToManyField(blank=True, related_name='item_locations', to='civam.PersonOrInstitute'),
        ),
        migrations.AddField(
            model_name='item',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to=civam.models.image_upload_path)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='civam.item')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='creator',
            field=models.ManyToManyField(blank=True, related_name='collection_creators', to='civam.PersonOrInstitute'),
        ),
        migrations.AddField(
            model_name='collection',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='collection_keywords', to='civam.Keyword'),
        ),
        migrations.AddField(
            model_name='collection',
            name='location_of_originals',
            field=models.ManyToManyField(blank=True, related_name='collection_locations', to='civam.PersonOrInstitute'),
        ),
        migrations.AddField(
            model_name='collection',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CollectionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('default', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='civam.collection')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='auth.group')),
            ],
            options={
                'unique_together': {('name', 'collection')},
            },
        ),
    ]
