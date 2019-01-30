# blog/urls.py
from django.conf.urls import url
from blog import views_cbv
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^cbv/new/$', views_cbv.post_new),
]
