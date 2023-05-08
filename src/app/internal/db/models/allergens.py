from django.db import models


class Allergen(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='id',
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=64,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Allergen'
        verbose_name_plural = 'Allergens'
