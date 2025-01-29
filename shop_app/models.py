from django.db import models

# Create your models here.

class Item_catg(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(Item_catg, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop", null=True, blank=True)
    price = models.FloatField(max_length=7)
    availability = models.BooleanField(default=True)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return str(self.name)
