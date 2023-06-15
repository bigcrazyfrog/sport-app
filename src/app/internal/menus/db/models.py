from django.db import models


class Menu(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='id',
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    allergen = models.ManyToManyField(
        to='Allergen',
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
