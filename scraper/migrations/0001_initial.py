# Generated by Django 4.2.2 on 2023-08-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StocksData',
            fields=[
                ('symbol', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('prevClose', models.FloatField()),
                ('openPrice', models.FloatField()),
                ('highPrice', models.FloatField()),
                ('lowClose', models.FloatField()),
                ('adjClose', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
