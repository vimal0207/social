# Generated by Django 3.1 on 2020-12-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('gender', models.CharField(max_length=5)),
                ('active', models.CharField(default=False, max_length=7)),
                ('password', models.CharField(max_length=10)),
                ('otp', models.IntegerField(default=0)),
            ],
        ),
    ]
