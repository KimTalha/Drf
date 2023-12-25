# Generated by Django 3.2.16 on 2023-12-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='attributes',
            field=models.JSONField(default={'data': 'value'}),
        ),
        migrations.AlterField(
            model_name='nft',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/nft/', null=True),
        ),
        migrations.AlterField(
            model_name='nft',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nft',
            name='ownership_history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nft',
            name='token_metadata_uri',
            field=models.URLField(blank=True),
        ),
    ]
