# Generated by Django 3.2 on 2021-07-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('badminton', 'badminton'), ('Women', 'Women'), ('Electonic Gadgets', 'Electronic gadgets'), ('Store', 'Store')], default='Men', max_length=200),
        ),
    ]
