# Generated by Django 4.2.1 on 2023-05-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemname',
            name='slug_name',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='itemname',
            name='shapeCode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
