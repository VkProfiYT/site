from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('video/', index_video),
    path('photo/', index_photo),
    path('<int:id>/', view_content)
]