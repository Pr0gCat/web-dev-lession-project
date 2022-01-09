# Generated by Django 3.2 on 2022-01-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takoeats', '0006_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, '待接單'), (1, '準備中'), (2, '等待外送'), (3, '外送中'), (4, '外送員已到達目的地'), (5, '完成'), (6, '取消')], default=0),
        ),
    ]
