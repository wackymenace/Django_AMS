# Generated by Django 3.2.6 on 2021-08-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0003_auto_20210826_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtype',
            old_name='priceRecovered',
            new_name='purchasePrice',
        ),
        migrations.AddField(
            model_name='itemtype',
            name='salePrice',
            field=models.IntegerField(null=True),
        ),
    ]
