# Generated by Django 5.1.4 on 2024-12-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeManager', '0005_alter_resume_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
