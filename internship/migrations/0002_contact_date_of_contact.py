# Generated by Django 2.2.14 on 2021-08-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_of_contact',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
