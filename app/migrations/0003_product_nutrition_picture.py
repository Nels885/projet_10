# Generated by Django 2.1.3 on 2018-12-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181218_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutrition_picture',
            field=models.URLField(null=True),
        ),
    ]