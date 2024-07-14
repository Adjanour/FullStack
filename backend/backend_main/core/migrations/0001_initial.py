# Generated by Django 5.0.3 on 2024-05-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymentMethod",
            fields=[
                ("pmtIdpk", models.AutoField(primary_key=True, serialize=False)),
                ("pmtName", models.CharField(max_length=100)),
                ("pmtDescription", models.CharField(max_length=255)),
                ("pmtCreatedDate", models.DateTimeField(auto_now_add=True)),
                ("pmtLastUpdateDate", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentStatus",
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
                ("status_name", models.CharField(max_length=50)),
                ("status_description", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("last_edited_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                ("pchIdpk", models.AutoField(primary_key=True, serialize=False)),
                ("pchPurchaseDate", models.DateTimeField()),
                (
                    "pchTotalAmount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("pchCreatedDate", models.DateTimeField(auto_now_add=True)),
                ("pchLastUpdateDate", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserAddressTable",
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
                ("address_location", models.CharField(max_length=255)),
                ("digital_address", models.CharField(max_length=255)),
                ("house_address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserTable",
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
                ("user_name", models.CharField(max_length=50)),
                ("user_password", models.CharField(max_length=50)),
                ("user_email", models.CharField(max_length=50)),
                ("user_date_of_birth", models.DateField()),
                ("user_phone_number", models.CharField(max_length=50)),
            ],
        ),
    ]
