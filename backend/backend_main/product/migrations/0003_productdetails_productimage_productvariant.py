# Generated by Django 5.0.3 on 2024-05-25 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(db_column='prdDetailsIdpk', primary_key=True, serialize=False)),
                ('weight', models.DecimalField(db_column='prdWeight', decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(db_column='prdLength', decimal_places=2, max_digits=10)),
                ('width', models.CharField(db_column='prdWidth', max_length=255)),
                ('height', models.CharField(db_column='prdHeight', max_length=255)),
                ('dimensions', models.CharField(db_column='prdDimensions', max_length=255)),
                ('techinical_specifications', models.TextField(db_column='prdTechnicalSpecifications')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='prdCreatedDate')),
                ('last_edit_date', models.DateTimeField(auto_now=True, db_column='prdLastEditDate')),
                ('product_id', models.ForeignKey(db_column='prdDetailsPrdIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(db_column='imgIdpk', primary_key=True, serialize=False)),
                ('url', models.URLField(db_column='imgURL')),
                ('descriptioin', models.TextField(db_column='imgDescription')),
                ('upload_date', models.DateTimeField(auto_now_add=True, db_column='imgUploadDate')),
                ('last_edit_date', models.DateTimeField(auto_now=True, db_column='imgLastEditDate')),
                ('product_id', models.ForeignKey(db_column='imgPrdIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(db_column='prvIdpk', primary_key=True, serialize=False)),
                ('prvColor', models.CharField(db_column='prvColor', max_length=100)),
                ('prvSize', models.CharField(db_column='prvSize', max_length=100)),
                ('prvMaterial', models.CharField(db_column='prvMaterial', max_length=100)),
                ('prvPriceModifier', models.DecimalField(db_column='prvPriceModifier', decimal_places=2, max_digits=10)),
                ('prvQuantityAvailable', models.IntegerField(db_column='prvQuantityAvailable')),
                ('prvSKU', models.CharField(db_column='prvSKU', max_length=100, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='prvCreatedDate')),
                ('last_edit_date', models.DateTimeField(auto_now=True, db_column='prvLastEditDate')),
                ('product_id', models.ForeignKey(db_column='prvPrdIdfk', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]