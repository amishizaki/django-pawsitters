# Generated by Django 4.1.3 on 2022-11-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_type_petowner_pet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='petowner',
            name='pet_bio',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
