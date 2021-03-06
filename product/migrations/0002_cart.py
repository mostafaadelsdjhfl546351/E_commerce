# Generated by Django 3.2.12 on 2022-05-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('products_list', models.ManyToManyField(blank=True, null=True, to='product.product')),
            ],
        ),
    ]
