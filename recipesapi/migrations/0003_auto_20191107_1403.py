# Generated by Django 2.2.6 on 2019-11-07 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapi', '0002_auto_20191105_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='itemURL',
            new_name='craftingURL',
        ),
    ]
