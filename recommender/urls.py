from django.conf.urls import include, url
from recommender import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
]