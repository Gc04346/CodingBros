from django.urls import path

from .views import homepage

app_name = 'tasks'
urlpatterns = [
    path('', homepage)
]
