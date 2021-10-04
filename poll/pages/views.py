from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#handles various webpages

def home_view(request,*args, **kwargs):
	my_context = {
		"my_text":"This is shit",
		"my_number":"123"
	}
	return render(request,"home.html",my_context)

def about_view(request):
	my_context = {
		"my_text":"This is shit",
		"my_number":"123",
		"my_list":[1,2,3,4,5,6],
		"my_html":"<h1>Jason Zuang</h1>"
	}

	return render(request, "about.html", my_context)