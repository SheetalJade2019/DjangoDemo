from django.urls import path
from .views import testcelery

urlpatterns = [
    path("testcelery/",testcelery, name="home")
]