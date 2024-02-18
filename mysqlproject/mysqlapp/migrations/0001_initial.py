# Generated by Django 5.0.1 on 2024-02-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.FloatField()),
                ('emobile', models.CharField(max_length=60)),
                ('eemail', models.CharField(max_length=40)),
                ('eaddress', models.CharField(max_length=100)),
            ],
        ),
    ]
