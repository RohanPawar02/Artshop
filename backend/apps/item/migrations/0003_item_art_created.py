# Generated by Django 3.2.6 on 2021-10-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='art_created',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Art Created'),
        ),
    ]