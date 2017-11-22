from django.conf.urls import url

from . import views

urlpatterns = [
    url('^main/', views.main, name = 'main'),
    url('^hello/(\w+)?', views.hello, name = 'hello'),
    url('^yyyymmdd/(?P<yyyy>\d{4})/(?P<mm>\d{2})/(?P<dd>\d{2})', views.yyyymmdd, name = 'yyyymmdd'),
]
