# Generated by Django 3.2.2 on 2021-05-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
