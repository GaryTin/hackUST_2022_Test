# Generated by Django 4.0.2 on 2022-02-21 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_alter_people_age_alter_people_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
