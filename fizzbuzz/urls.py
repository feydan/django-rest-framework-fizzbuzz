from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fizzbuzz import views

urlpatterns = [
    url(r'^fizzbuzz/$', views.FizzBuzzList.as_view()),
    url(r'^fizzbuzz/(?P<pk>[0-9]+)/$', views.FizzBuzzDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)