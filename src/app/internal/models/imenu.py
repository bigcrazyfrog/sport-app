from django.db import models
from app.internal.models.products import Product


class IMenu(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='id',
        primary_key=True,
    )
    breakfast = models.ForeignKey(
        'Product',
        related_name='breakfast',
        on_delete=models.CASCADE,
    )
    lunch = models.ForeignKey(
        'Product',
        related_name='lunch',
        on_delete=models.CASCADE,
    )
    dinner = models.ForeignKey(
        'Product',
        related_name='dinner',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id}: {self.breakfast}, {self.lunch}, {self.dinner}"


class Gluten(IMenu):
    class Meta:
        verbose_name = 'Gluten'
        verbose_name_plural = 'MenuGlutens'


class Lactose(IMenu):
    class Meta:
        verbose_name = 'Lactose'
        verbose_name_plural = 'MenuLactose'


class Lectins(IMenu):
    class Meta:
        verbose_name = 'Lectins'
        verbose_name_plural = 'MenuLectins'
