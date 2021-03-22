from django.contrib import admin
from .models import hotels,things,restaurants,flights


# Register your models here.

admin.site.register(hotels)
admin.site.register(things)
admin.site.register(restaurants)
admin.site.register(flights)
