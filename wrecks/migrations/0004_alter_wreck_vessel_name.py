# Generated by Django 4.1.3 on 2022-12-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0003_alter_wreck_beavertail_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wreck',
            name='vessel_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
