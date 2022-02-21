# Generated by Django 4.0.2 on 2022-02-21 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0004_people_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(choices=[('ICT', 'Information and Communication Technologies'), ('PHY', 'Physics'), ('BIO', 'Biology'), ('ECO', 'Economics'), ('CSE', 'Computer Science and Engineering')], default='ICT', max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TestApp.teacher'),
        ),
    ]
