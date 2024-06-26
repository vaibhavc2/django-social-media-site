# Generated by Django 3.0.5 on 2022-02-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=15, null=True)),
                ('FirstName', models.CharField(max_length=150, null=True)),
                ('LastName', models.CharField(max_length=150, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('Contact', models.CharField(max_length=15, null=True)),
                ('Gender', models.CharField(max_length=15, null=True)),
                ('Hobbies', models.CharField(max_length=150, null=True)),
                ('placeofBirth', models.CharField(max_length=200, null=True)),
                ('placeofWork', models.CharField(max_length=150, null=True)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=300, null=True)),
                ('CreationDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
