from django.db import models


class ProductOrder(models.Model):
    name = models.ForeignKey(
        'crm.Order',
        on_delete=models.PROTECT,
        verbose_name='название',
        related_name='orders'
    )
    is_active = models.BooleanField(default=True)
    is_specification_done = models.BooleanField(default=True)

    def __str__(self):
        return self.name.title
