from django.db import models


class ProductOrder(models.Model):
    name = models.OneToOneField(
        'crm.Product',
        on_delete=models.PROTECT,
        verbose_name='название',
        related_name='products',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_specification_done = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.name.
