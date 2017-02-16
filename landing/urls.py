from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    # url(r'^landing/', views.landing, name= 'landing'),
    # url(r'^landing/search/$', views.search, name= 'search'),
    # url(r'^landing/create/$', views.create, name= 'create'),
]