# Generated by Django 4.1.2 on 2022-10-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to read more', max_length=15),
        ),
    ]
