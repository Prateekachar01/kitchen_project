# Generated by Django 5.0.2 on 2024-03-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfood', '0005_rename_fooffile_addfood_foodfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfood',
            name='foodFile',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/'),
        ),
    ]
