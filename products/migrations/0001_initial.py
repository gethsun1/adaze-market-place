# Generated by Django 5.2.dev20241120122318 on 2024-11-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('children', 'Children'), ('men', 'Men'), ('women', 'Women'), ('unisex', 'Unisex'), ('accessories', 'Accessories')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]
