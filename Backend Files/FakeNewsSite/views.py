from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'FakeNewsSite/Home.html')
	
def about(request):
	return render(request, 'FakeNewsSite/About.html')
# Create your views here.
