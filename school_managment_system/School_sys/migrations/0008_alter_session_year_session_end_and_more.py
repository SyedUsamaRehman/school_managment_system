# Generated by Django 4.1.7 on 2023-03-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0007_rename_session_end_session_year_session_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_year',
            name='Session_end',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='session_year',
            name='Session_start',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
