# Generated by Django 3.2.16 on 2024-09-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_relative_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]