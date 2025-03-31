# Generated by Django 5.1.7 on 2025-03-31 13:18

import django.db.models.deletion
import django_extensions.db.fields
import snap.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(upload_to=snap.models._upload_to)),
                ('snap', models.CharField(default=snap.models._generate_random_unique_snap_name, max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Snap',
                'verbose_name_plural': 'Snaps',
            },
        ),
    ]
