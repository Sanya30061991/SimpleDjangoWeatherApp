from django.db import models

# Create your models here.

class Req(models.Model):
    r = models.CharField('Request for weather', max_length=100)

    def __str__(self):
        return self.r
        
    class Meta():
        verbose_name = "Request"
        verbose_name_plural = "Requests"