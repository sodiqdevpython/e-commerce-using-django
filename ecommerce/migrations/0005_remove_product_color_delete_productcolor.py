# Generated by Django 5.0.4 on 2024-05-08 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_productcolor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
    ]
