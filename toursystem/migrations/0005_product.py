# Generated by Django 3.0.3 on 2020-02-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursystem', '0004_auto_20200226_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
    ]
