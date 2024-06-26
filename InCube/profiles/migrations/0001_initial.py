# Generated by Django 5.0.4 on 2024-05-10 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discordId', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('roleId', models.IntegerField(default=1)),
                ('avatar', models.ImageField(blank=True, upload_to='media/avatar/')),
                ('links', models.JSONField(blank=True, null=True)),
                ('socialCredits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('maxBio', models.IntegerField(default=512)),
                ('isAvatarAvailable', models.BooleanField(default=False)),
                ('canAddLinks', models.BooleanField(default=False)),
                ('canPublishContent', models.BooleanField(default=False)),
                ('canEditContent', models.BooleanField(default=False)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.users')),
                ('bio', models.TextField()),
                ('chanels', models.JSONField(default=dict, null=True)),
            ],
            bases=('profiles.users',),
        ),
    ]
