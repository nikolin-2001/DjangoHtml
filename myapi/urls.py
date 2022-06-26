from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Shoes', views.ShoesViewSet)
router.register(r'Jeans', views.JeansViewSet)
router.register(r'Tshirt', views.TshirtViewSet)
router.register(r'Sweatshirts', views.SweatshirtsViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('catalog/', views.PashalkaoneCreate.as_view(), name='Catalog'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
