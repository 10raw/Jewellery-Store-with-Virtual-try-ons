# Generated by Django 3.1.4 on 2021-08-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldpage', '0013_auto_20210704_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='usrfullname',
            field=models.CharField(default='FirstName LastName', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='usraddress',
            field=models.CharField(max_length=500),
        ),
    ]
