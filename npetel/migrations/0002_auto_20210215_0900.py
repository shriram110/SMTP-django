# Generated by Django 3.1.6 on 2021-02-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npetel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='courseCode',
            field=models.CharField(max_length=20),
        ),
    ]
