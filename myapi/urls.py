from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.PreviewCreate.as_view(), name='preview'),
    path('open/<slug:shoes_slug>/', views.product_open, name='open'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
