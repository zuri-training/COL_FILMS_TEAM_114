# Generated by Django 4.0.6 on 2022-08-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar/', verbose_name='Avatar'),
        ),
    ]
