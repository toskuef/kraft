from django.db import models


class TypeStorage(models.Model):
    name = models.CharField(max_length=150, verbose_name='тип склада')

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=150, verbose_name='название склада')
    type_storage = models.ForeignKey(
        TypeStorage,
        on_delete=models.PROTECT,
        verbose_name='тип склада',
        related_name='storage'
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='категория')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=150, verbose_name='группа')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='категория'
    )

    def __str__(self):
        return self.name


class Nomenclature(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        verbose_name='группа'
    )

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    address = models.CharField(max_length=255, verbose_name='адрес')
    manager = models.CharField(max_length=255, verbose_name='менеджер')
    manager_phone = models.IntegerField(verbose_name='телефон менеджера')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    nomenclature = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        related_name='purchase',
        verbose_name='номенклатура'
    )
    contractor = models.ForeignKey(
        Contractor,
        on_delete=models.PROTECT,
        related_name='purchase',
        verbose_name='поставщик',
        blank=True,
        null=True
    )
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    storage = models.ForeignKey(
        Storage,
        on_delete=models.PROTECT,
        related_name='purchase',
        verbose_name='склад',
        blank=True,
        null=True
    )
    is_order = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nomenclature} + {self.count}'


class Specification(models.Model):
    order = models.ForeignKey(
        'production.ProductOrder',
        on_delete=models.CASCADE,
        related_name='specification',
        verbose_name='заказ на производство'
    )
    nomenclature = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        related_name='specification',
        verbose_name='номенклатура'
    )
    count = models.PositiveSmallIntegerField()
    is_booking = models.BooleanField(default=False)
    is_order = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.order.name} - {self.nomenclature} + {self.count}'

