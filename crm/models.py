from django.db import models


class Customer(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    family_name = models.CharField(max_length=100, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    source = models.ForeignKey(
        'SourceCustomer',
        related_name='customers',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Источник',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.family_name}'


class SourceCustomer(models.Model):
    source = models.CharField(max_length=15, verbose_name='Источник')

    def __str__(self):
        return self.source


class Address(models.Model):
    customer = models.ManyToManyField(
        'Customer',
        verbose_name='клиенты',
        related_name='addresses',
        blank=True,
    )
    country = models.ForeignKey(
        'AddressCountry',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='страна',
    )
    area = models.ForeignKey(
        'AddressArea',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='область',
    )
    region = models.ForeignKey(
        'AddressRegion',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='район',
    )
    town = models.ForeignKey(
        'AddressTown',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='город',
    )
    street = models.ForeignKey(
        'AddressStreet',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='улица',
    )
    num_house = models.IntegerField(verbose_name='номер дома', blank=True)
    num_housing = models.IntegerField(verbose_name='номер корпуса', blank=True)
    num_door = models.IntegerField(verbose_name='номер подъезда', blank=True)
    num_level = models.IntegerField(verbose_name='номер этажа', blank=True)
    num_flat = models.IntegerField(verbose_name='номер квартиры', blank=True)

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return (f'{self.country}, {self.area}, {self.region}, {self.town}, '
                f'{self.street}, {self.num_house}, {self.num_housing}, '
                f'{self.num_door}, {self.num_level}, {self.num_flat}')


class AddressCountry(models.Model):
    title = models.CharField(verbose_name='назавние страны', max_length=100)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.title


class AddressArea(models.Model):
    title = models.CharField(verbose_name='назавние области', max_length=100)

    class Meta:
        verbose_name = 'область'
        verbose_name_plural = 'области'

    def __str__(self):
        return self.title


class AddressRegion(models.Model):
    title = models.CharField(verbose_name='название района', max_length=100)

    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'районы'

    def __str__(self):
        return self.title


class AddressTown(models.Model):
    title = models.CharField(verbose_name='название города', max_length=100)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.title


class AddressStreet(models.Model):
    title = models.CharField(verbose_name='название улицы', max_length=100)

    class Meta:
        verbose_name = 'улица'
        verbose_name_plural = 'улицы'

    def __str__(self):
        return self.title


class Order(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    price = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='сумма заказа')
    pre_pay = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='предоплата')
    second_pay = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='второй взнос', blank=True)
    pre_pay_type = models.ForeignKey(
        'TypePay',
        related_name='pre_pay_types',
        on_delete=models.PROTECT,
        verbose_name='тип предоплаты',
    )
    second_pay_type = models.ForeignKey(
        'TypePay',
        related_name='second_pay_types',
        on_delete=models.PROTECT,
        verbose_name='тип второго платежа',
        blank=True,
        null=True,
    )
    date_create = models.DateField(auto_now_add=True)
    date_done = models.DateField()
    date_pre_pay = models.DateField()
    date_second_pay = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(
        'Customer',
        related_name='orders',
        on_delete=models.PROTECT,
        verbose_name='клиент',
    )

    def __str__(self):
        return self.title


class TypePay(models.Model):
    type_pay = models.CharField(max_length=150, verbose_name='тип оплаты')

