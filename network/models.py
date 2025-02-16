from django.db import models


class NetworkNode(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название звена сети",
    )
    email = models.EmailField(
        verbose_name="Email", help_text="Контактный email"
    )
    country = models.CharField(
        max_length=100, verbose_name="Страна", help_text="Страна расположения"
    )
    city = models.CharField(
        max_length=100, verbose_name="Город", help_text="Город расположения"
    )
    street = models.CharField(
        max_length=100, verbose_name="Улица", help_text="Улица расположения"
    )
    house_number = models.CharField(
        max_length=10, verbose_name="Номер дома", help_text="Номер дома"
    )
    supplier = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="clients",
        verbose_name="Поставщик",
        help_text="Поставщик оборудования",
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Задолженность",
        help_text="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
        help_text="Время создания записи",
    )

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Название продукта"
    )
    model = models.CharField(
        max_length=100, verbose_name="Модель", help_text="Модель продукта"
    )
    release_date = models.DateField(
        verbose_name="Дата выхода на рынок",
        help_text="Дата выхода продукта на рынок",
    )
    network_node = models.ForeignKey(
        NetworkNode,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Звено сети",
        help_text="Звено сети, к которому относится продукт",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
