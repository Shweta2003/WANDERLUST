from django.db import models
from travello.models import Destination
# Create your models here.
class Destination(models.Model):

    name=models.ForeignKey(Destination.name,on_delete=models.SET_DEFAULT,on_update=models.SET_DEFAULT)
    img=models.ForeignKey(Destination.img,on_delete=models.SET_DEFAULT,on_update=models.SET_DEFAULT)
    desc=models.ForeignKey(Destination.desc,on_delete=models.SET_DEFAULT,on_update=models.SET_DEFAULT)
    price=models.ForeignKey(Destination.price,on_delete=models.SET_DEFAULT,on_update=models.SET_DEFAULT)
    offer=models.BooleanField(default=False)
    hotels=models.CharField(max_length=200)
