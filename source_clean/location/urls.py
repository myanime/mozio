from django.conf.urls import url
from location import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.PostLocation.as_view(), name='post-info'),
    url(r'(?P<pk>[0-9]+)/$', views.QueryLocation.as_view(), name='get-list'),
]
