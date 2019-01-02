# Generated by Django 2.1.3 on 2019-01-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_nutrition_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
