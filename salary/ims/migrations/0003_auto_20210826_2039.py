# Generated by Django 3.2.6 on 2021-08-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0002_auto_20210826_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
