from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField

from shop_app.models import Item

# Create your models here.

User=get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True)

    class Meta:
        db_table = "orders"
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.ordertext_set.aggregate(
            total=Sum(F("price")*F("quantity"), output_field= FloatField())
        )["total"]

class Order_text(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)

    class Meta:
        db_table = "ordertext"
        verbose_name = 'ordertext'
        verbose_name_plural = 'ordertexts'
        ordering = ["id"]

    def __str__(self):
        return f'{self.quantity} units of {self.item.name}'

    @property
    def total(self):
        pass