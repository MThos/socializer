# Generated by Django 3.1 on 2020-09-02 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('signup', models.DateTimeField(default=datetime.date(2020, 9, 1))),
                ('logins', models.IntegerField(default=0)),
                ('last_login', models.DateTimeField(default=datetime.date(2020, 9, 1))),
            ],
        ),
    ]
