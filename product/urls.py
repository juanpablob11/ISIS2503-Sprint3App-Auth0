from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('products/', views.product_list, name='productList'),
    path('productcreate/', csrf_exempt(views.product_create), name='productCreate'),
]
