# Generated by Django 3.0.2 on 2020-04-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='nature',
            field=models.CharField(max_length=50, verbose_name='Subject Nature'),
        ),
    ]
