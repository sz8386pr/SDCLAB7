from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),    # if url is index/base, invoke place_list() from the views.py
    url(r'^visited$', views.places_visited, name='places_visited'), # if url is visited, invoke places_visited() from the views.py
    url(r'^place/(?P<pk>\d+)/$', views.place_detail, name='place_detail'),
]
