# blog/urls.py
from django.conf.urls import url
from blog import views_cbv
from . import views

urlpatterns = [
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^detail/(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^cbv/new/$', views_cbv.post_new),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete),
]
