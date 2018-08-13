from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "app/index.html")

def about(request):
	return HttpResponse("About page")

def photos(request):
	return HttpResponse("Photo Spots")

def guides(request):
	return HttpResponse("Guides")

def video(request):
	return HttpResponse("Video Editing")

def payment(request):
	return HttpResponse("Payment")