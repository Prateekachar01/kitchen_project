# Generated by Django 5.0.2 on 2024-03-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=55, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('userId', models.CharField(blank=True, max_length=15, null=True)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('kitchenName', models.CharField(blank=True, max_length=115, null=True)),
            ],
        ),
    ]
