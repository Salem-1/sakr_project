# Generated by Django 3.2.2 on 2021-06-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_rename_aticles_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='articles',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
