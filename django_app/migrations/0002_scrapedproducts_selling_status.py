# Generated by Django 5.1.1 on 2024-09-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapedproducts',
            name='selling_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
