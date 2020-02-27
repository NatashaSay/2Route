# Generated by Django 3.0.3 on 2020-02-26 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('toursystem', '0008_product_productcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProductCat',
            new_name='City',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='route',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursystem.City'),
        ),
    ]