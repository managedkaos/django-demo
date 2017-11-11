from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bootstrap_template, name='bootstrap_template'),
]
