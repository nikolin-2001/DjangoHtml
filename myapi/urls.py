from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Shoes', views.ShoesViewSet)
router.register(r'Jeans', views.JeansViewSet)
router.register(r'Tshirt', views.TshirtViewSet)
router.register(r'Sweatshirts', views.SweatshirtsViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]