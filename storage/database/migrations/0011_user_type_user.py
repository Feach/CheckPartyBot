# Generated by Django 4.1.7 on 2023-04-24 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_party_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_user',
            field=models.CharField(default='Пользователь', max_length=50),
        ),
    ]