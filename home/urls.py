from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('dwn/', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/',
         views.download_cheatsheet, name='download_cheatsheet'),
]
