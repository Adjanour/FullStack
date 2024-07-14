# Generated by Django 5.0.3 on 2024-05-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SupplierTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("supplier_name", models.CharField(max_length=100)),
                ("supplier_contact_info", models.CharField(max_length=255)),
                ("supplier_address_line1", models.CharField(max_length=255)),
                ("supplier_address_line2", models.CharField(max_length=255)),
                ("supplier_city", models.CharField(max_length=100)),
                ("supplier_state", models.CharField(max_length=100)),
                ("supplier_postal_code", models.CharField(max_length=20)),
                ("supplier_country", models.CharField(max_length=100)),
            ],
        ),
    ]
