# Generated by Django 4.1.7 on 2023-04-12 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School_sys', '0020_remove_subject_teacher_subject_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('CLass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_sys.s_clas')),
                ('Session_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_sys.session_year')),
                ('Teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_sys.teachers')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_sys.subject')),
            ],
        ),
    ]
