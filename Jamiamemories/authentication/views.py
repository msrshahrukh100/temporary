from django.shortcuts import render

# Create your views here.

def home_page(request) :
	return render(request,'homepage.html',{})


def user_dashboard(request) :
	return render(request,'userdashboard.html',{})