
from django.conf.urls import url
from .views import (
#     product_list_view,
    ProductListView,
#     ProductDetailView,
    ProductDetailSlugView,
#     product_detail_view,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView,
)

app_name = 'products'
urlpatterns = [
    url(r'^$',ProductListView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),    
]
