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
    breakfast = models.ManyToManyField(
        to='Product',
        related_name='breakfast',
        blank=True,
        symmetrical=False,
    )
    lunch = models.ManyToManyField(
        to='Product',
        related_name='lunch',
        blank=True,
        symmetrical=False,
    )
    dinner = models.ManyToManyField(
        to='Product',
        related_name='dinner',
        blank=True,
        symmetrical=False,
    )

    kalo_sum = models.PositiveIntegerField(default=0)

    def _get_kalo_sum(self):
        s = sum(self.breakfast.all().values_list("kilocalories", flat=True))
        s += sum(self.lunch.all().values_list("kilocalories", flat=True))
        s += sum(self.dinner.all().values_list("kilocalories", flat=True))

        return s

    def save(self, *args, **kwargs):
        self.kalo_sum = self._get_kalo_sum()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu}: {self.day}"

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'
