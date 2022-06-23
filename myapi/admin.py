from django.contrib import admin
from .models import Shoes, Jeans, Tshirt, Sweatshirts

admin.site.register(Sweatshirts)
admin.site.register(Jeans)
admin.site.register(Shoes)
admin.site.register(Tshirt)