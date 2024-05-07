from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clients/', views.cliente_list, name='clienteList'),
    path('client/<int:id>/', views.single_cliente, name='singleCliente'),
    path('clientcreate/', csrf_exempt(views.cliente_create), name='clienteCreate'),
]
