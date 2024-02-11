from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('download/<int:cv_id>/',
         views.download_cv, name='download_cv'),
]
