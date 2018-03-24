from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.set_categories, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.get_categories, name='get_categories'),
]