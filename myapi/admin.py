from django.contrib import admin
from .models import Shoes, Jeans, Tshirt, Sweatshirts, Size, Category

admin.site.register(Sweatshirts)
admin.site.register(Jeans)
admin.site.register(Shoes)
admin.site.register(Tshirt)
admin.site.register(Size)
admin.site.register(Category)