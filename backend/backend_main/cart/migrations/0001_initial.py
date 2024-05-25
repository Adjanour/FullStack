# Generated by Django 4.0 on 2024-05-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('crtIdpk', models.AutoField(primary_key=True, serialize=False)),
                ('crtCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('crtStatus', models.CharField(default='Active', max_length=50)),
                ('crtCustomerIdfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customertable')),
            ],
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
