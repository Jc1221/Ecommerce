from django.conf.urls import url
from . import views

app_name = 'merchants'
urlpatterns = [
    url(r'^$', views.merchant_dashboard, name='dashboard'),
    url(r'^products/$', views.merchant_product_list, name='product_list'),
    url(r'^products/create/$', views.merchant_product_create, name='product_create'),
    url(r'^products/(?P<product_id>\d+)/edit/$', views.merchant_product_edit, name='product_edit'),
    url(r'^products/(?P<product_id>\d+)/delete/$', views.merchant_product_delete, name='product_delete'),
    url(r'^products/(?P<product_id>\d+)/toggle/$', views.merchant_product_toggle_active, name='product_toggle'),
]