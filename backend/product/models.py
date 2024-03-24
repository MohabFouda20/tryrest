from django.db import models
from django.conf import settings



User = settings.AUTH_USER_MODEL # This is the same as from django.contrib.auth import get_user_model
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User , on_delete = models.SET_NULL , null=True , default=1)
    title = models.CharField(max_length=120)
    content = models.TextField( blank=True , null=True)
    price = models.DecimalField(decimal_places=2 , max_digits=15 , default=0.00)
    @property
    def sale(self):
        return self.price*10