# Generated by Django 3.1.6 on 2021-05-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='media/images/defaultprofilepicture.png', max_length=1000, upload_to='images'),
        ),
    ]
