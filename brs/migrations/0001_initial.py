# Generated by Django 4.1.4 on 2023-03-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_s', models.CharField(max_length=20)),
                ('to_s', models.CharField(max_length=20)),
            ],
        ),
    ]
