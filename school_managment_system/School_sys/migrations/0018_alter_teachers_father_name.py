# Generated by Django 4.1.7 on 2023-04-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0017_student_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='Father_Name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
