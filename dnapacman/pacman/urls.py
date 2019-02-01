from django.conf.urls import url
from pacman import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
