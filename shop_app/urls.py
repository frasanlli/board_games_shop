from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop/category/<int:category_id>/',
         views.category_filter, name='item_category'),
    path('shop/add/<int:item_id>/',
         views.add_item, name='add_item'),
    path('shop/substract/<int:item_id>/',
         views.substract_item, name='substract_item'),
    path('shop/delete/<int:item_id>/',
         views.delete_item, name='delete_item'),
    path('shop/clean_cart/<int:item_id>/',
         views.clean_cart, name='clean_cart'),
]

urlpatterns+=static(settings.MEDIA_URL,
                    document_root = settings.MEDIA_ROOT)

