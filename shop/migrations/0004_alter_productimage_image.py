# Generated by Django 4.1.7 on 2024-03-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_slug_alter_productcategory_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.URLField(),
        ),
    ]