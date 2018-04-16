from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.index),
	path('About/', views.about)
]

# Create your views here.
