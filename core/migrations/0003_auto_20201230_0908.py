# Generated by Django 3.1.4 on 2020-12-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.TextField(default='', null=True),
        ),
    ]