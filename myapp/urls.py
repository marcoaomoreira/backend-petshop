from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^canils/$', views.CanilList.as_view(), name='canil-list'),
    url(r'^canil/(?P<pk>[0-9]+)/$', views.CanilDetail.as_view(), name='canil-detail'),

]