# Generated by Django 2.0.4 on 2019-09-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_merge_20190801_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]