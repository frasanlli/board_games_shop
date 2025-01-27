from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='service_app')
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return str(self.title)

