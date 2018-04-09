from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.index)
]

# Create your views here.
