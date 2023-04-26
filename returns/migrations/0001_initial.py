# Generated by Django 4.1.7 on 2023-04-26 12:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Return",
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
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("vat_tax", models.IntegerField(default=0)),
                ("qty", models.PositiveIntegerField()),
                ("discount", models.PositiveIntegerField(default=0)),
                ("other_cost", models.PositiveIntegerField(default=0)),
                ("shipping_cost", models.PositiveIntegerField(default=0)),
                ("grand_total", models.PositiveIntegerField(default=0)),
                ("note", models.TextField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
