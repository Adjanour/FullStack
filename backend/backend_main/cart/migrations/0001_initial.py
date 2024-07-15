# Generated by Django 4.0 on 2024-05-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(db_column='crtIdpk', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='crtCreatedAt')),
                ('cart_status', models.CharField(db_column='crtStatus', default='Active', max_length=50)),
            ],
            options={
                'db_table': 'tblCarts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('crtItemIdpk', models.AutoField(primary_key=True, serialize=False)),
                ('crtItemQuantity', models.IntegerField()),
                ('crtItemUnitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('crtItemCrtIdfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('crtItemPrdIdfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
