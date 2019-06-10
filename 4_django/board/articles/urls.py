from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # Read
    path('', views.index, name="index"),
    path('<int:article_id>/', views.detail, name="detail"),

    # Create
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]

