# Generated by Django 4.1.7 on 2023-05-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_statisticpartydelete_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statisticpartydelete',
            name='choice',
        ),
        migrations.AddField(
            model_name='party',
            name='choice',
            field=models.CharField(default=123124124, max_length=50),
            preserve_default=False,
        ),
    ]
