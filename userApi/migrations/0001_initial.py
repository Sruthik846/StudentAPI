# Generated by Django 4.2.2 on 2023-06-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
                ('mobileNo', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]