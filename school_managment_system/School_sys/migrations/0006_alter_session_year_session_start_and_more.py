# Generated by Django 4.1.7 on 2023-03-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0005_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_year',
            name='Session_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='session_year',
            name='session_end',
            field=models.DateField(null=True),
        ),
    ]