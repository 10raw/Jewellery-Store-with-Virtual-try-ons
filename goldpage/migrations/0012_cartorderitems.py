# Generated by Django 3.1.4 on 2021-07-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goldpage', '0011_cartorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldpage.cartorder')),
            ],
        ),
    ]
