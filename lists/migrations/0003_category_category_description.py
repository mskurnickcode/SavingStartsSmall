# Generated by Django 3.1.3 on 2021-01-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20210123_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.TextField(default=''),
        ),
    ]