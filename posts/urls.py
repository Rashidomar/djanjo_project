from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns =[
    #/index/ 
    url(r'^$', views.index, name='index'),
    #/upload/
    url(r'^upload/', views.upload, name='upload' ),
    #/cat/
    url(r'^cat/', views.product_category, name='category'),
    #url(r'^name/', views.name),
    #/product/312/
    url(r'^(?P<cat_id>[0-9]+)/$', views.product_detail, name='detail'),

    url(r'^accounts/profile/(?P<product_id>[0-9]+)/$', views.product_delete, name='delete'),
    
]