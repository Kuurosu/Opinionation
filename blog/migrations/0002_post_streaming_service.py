# Generated by Django 3.2.18 on 2023-04-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='streaming_service',
            field=models.CharField(choices=[('Netflix', 'Netflix'), ('Prime', 'Prime'), ('Apple TV', 'Apple TV')], default='NETFLIX', max_length=10),
        ),
    ]
