from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getprice/', views.getprice, name='getprice'),
    url(r'^adddat/$', views.savedat, name='savedat'),
#    url(r'^predict', views.predict, name='predict'),
]
