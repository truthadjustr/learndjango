from django.conf.urls import url

from . import views

urlpatterns = [
    url('^main/', views.main, name = 'main'),
    url('^hello/(\w+)?', views.hello, name = 'hello'),
]
