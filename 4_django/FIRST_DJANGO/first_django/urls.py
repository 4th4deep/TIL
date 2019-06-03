from django.contrib import admin
from django.urls import path

from . import views as master_views
from home import views as home_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('hello/<str:name>/', views.hello),
    path('home/', home_views.home_index)
]
