from django.urls import path

from . import views

urlpatterns = [
    path("",views.list, name="news list"),
    path("<int:news_id>/", views.detail, name="news detail"),
]