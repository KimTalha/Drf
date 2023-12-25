from django.urls import path
from . import views

urlpatterns = [
    path("fetch/record/", views.NFTView.as_view()),
    path("add/record/", views.NFTView.as_view()),
    path("edit/record/<int:id>/", views.NFTView.as_view()),
    path("remove/record/<int:id>/", views.NFTView.as_view())
]