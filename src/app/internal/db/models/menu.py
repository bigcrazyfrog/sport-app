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


class Recommendation(models.Model):
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE,
    )
    day = models.PositiveIntegerField(
        verbose_name='day',
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

    kalo_sum = models.PositiveIntegerField(default=0)

    def _get_kalo_sum(self):
        return self.breakfast.kilocalories + self.lunch.kilocalories + self.dinner.kilocalories

    def save(self, *args, **kwargs):
        self.kalo_sum = self._get_kalo_sum()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu}: {self.day}"

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'
