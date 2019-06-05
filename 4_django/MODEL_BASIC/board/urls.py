from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('new/', views.new_article),  # /board/new/
    path('create/', views.create_article),  # /board/create/
    path('', views.article_list),  # /board/
    path('<int:article_id>/', views.article_detail),  # /board/2/

]
