from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.save_embed, name='index'),
]
