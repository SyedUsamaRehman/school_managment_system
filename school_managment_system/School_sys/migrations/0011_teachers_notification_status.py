# Generated by Django 4.1.7 on 2023-04-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0010_teachers_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_notification',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
