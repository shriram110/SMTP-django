# Generated by Django 3.1.6 on 2021-02-15 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('npetel', '0003_learnermodel_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnermodel',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='npetel.coursemodel'),
        ),
    ]
