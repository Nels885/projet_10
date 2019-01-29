# Generated by Django 2.1.5 on 2019-01-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('nutrition_grades', models.CharField(max_length=10)),
                ('nutrition_picture', models.URLField(null=True)),
                ('url', models.URLField()),
                ('front_picture', models.URLField(null=True)),
                ('category', models.URLField()),
            ],
        ),
    ]
