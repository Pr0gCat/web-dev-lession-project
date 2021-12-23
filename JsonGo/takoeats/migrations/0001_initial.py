# Generated by Django 3.2 on 2021-12-23 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=64)),
                ('created_on', models.DateField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('rating_count', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takoeats.users')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=64)),
                ('delivery_id', models.CharField(max_length=64)),
                ('order_time', models.TimeField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takoeats.status')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=64)),
                ('item_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takoeats.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField()),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takoeats.shops')),
            ],
        ),
    ]
