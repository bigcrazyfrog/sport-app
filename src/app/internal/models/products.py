from django.db import models


class Product(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=32,
    )
    kilocalories = models.PositiveIntegerField(
        verbose_name='Kilocalories',
        null=False,
        default=0,
    )
    proteins = models.DecimalField(
        verbose_name='Proteins',
        max_digits=8,
        decimal_places=1,
        null=False,
        default=0,
    )
    fats = models.DecimalField(
        verbose_name='Fats',
        max_digits=8,
        decimal_places=1,
        null=False,
        default=0,
    )
    carb = models.DecimalField(
        verbose_name='Carbohydrates',
        max_digits=8,
        decimal_places=1,
        null=False,
        default=0,
    )
    allergens = models.ManyToManyField(
        to='Allergen',
        verbose_name='Allergen list',
        symmetrical=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
