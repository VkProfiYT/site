# Generated by Django 5.0.4 on 2024-05-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('salesAmount', models.PositiveIntegerField(default=0)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
    ]
