# Generated by Django 3.2.2 on 2021-05-12 08:28

from django.db import migrations, models
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to=feed.models.post_pic),
        ),
    ]
