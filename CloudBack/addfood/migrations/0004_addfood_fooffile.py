# Generated by Django 5.0.2 on 2024-03-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0003_rename_delivertime_addfood_orderfrom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addfood',
            name='foofFile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
