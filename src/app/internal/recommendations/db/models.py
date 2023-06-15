from django.db import models


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
        kalo_sum = 0
        for product in self.breakfast.all().values("kilocalories", "proportion"):
            kalo_sum += product.kilocalories * product.proportion
        for product in self.lunch.all().values("kilocalories", "proportion"):
            kalo_sum += product.kilocalories * product.proportion
        for product in self.breakfast.all().values("kilocalories", "proportion"):
            kalo_sum += product.kilocalories * product.proportion

        return kalo_sum

    def _set_kalo_sum(self):
        self.kalo_sum = self._get_kalo_sum()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._set_kalo_sum()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.menu}: {self.day}"

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

        indexes = [
            models.Index(fields=['menu', 'day']),
        ]
