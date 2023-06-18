# Generated by Django 4.1.7 on 2023-04-07 22:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0009_alter_student_s_class_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_sys.teachers')),
            ],
        ),
    ]
