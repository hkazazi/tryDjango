from django.contrib import admin
from django.urls import path
from pages.views import home_view , contact_view
from products.views import (product_detail_veiw,
                            product_create_view,
                            dynamic_view)
urlpatterns = [
    path('<int:my_id>/',dynamic_view,name='product'),
    path('',product_detail_veiw),
    path('create/',product_create_view),
]