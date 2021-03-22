from django.db import models

class hotels(models.Model):
    name=models.CharField(max_length=200)
    name_hotel=models.CharField(max_length=200)
    price=models.IntegerField(default=1000)
    img=models.ImageField(upload_to='pics',default='')
    def get_absolute_url(self):
        return "hotels/{self.id}"

class things(models.Model):
    name=models.CharField(max_length=200)
    things=models.TextField()
    desc=models.TextField(default='')
    pics=models.ImageField(upload_to='pics',default='')
    def get_absolute_url(self):
        return "hotels/{self.id}"

class restaurants(models.Model):
    name=models.CharField(max_length=200)
    restaurant=models.CharField(max_length=400)
    famous=models.TextField()
    start=models.CharField(max_length=50)
    end=models.CharField(max_length=50)
    ratings=models.CharField(max_length=20)
    phone=models.IntegerField()
    price=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

class flights(models.Model):
    name=models.CharField(max_length=200,default='NOT FOUND')
    From=models.CharField(max_length=200,default='New Delhi')
    To=models.CharField(max_length=200,default='Canada')
    hours=models.CharField(max_length=200,default='06')
    price=models.CharField(max_length=400,default='Rs.30000.00')
    nameof=models.CharField(max_length=200,default='Indian Internationals')