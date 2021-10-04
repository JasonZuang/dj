from django.shortcuts import render, get_object_or_404
from .models import Dogs
from .forms import Dogs_Forms, Raw_Dogs_Form
# Create your views here.

def dynamic_lookup_view(request,my_id):
	obj = get_object_or_404(Dogs,id=my_id)
	context = {
		"object" : obj
	}
	return render(request, "dogs/dogs_detail.html",context)
def dogs_create_view(request):
	form = Raw_Dogs_Form()
	if request.method == 'POST':
		form = Raw_Dogs_Form(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Dogs.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, "dogs/dogs_detail.html",context)

# def dogs_create_view(request):
# 	print(request.POST)
# 	context = {

# 	}
# 	return render(request, "dogs/dogs_detail.html",context)

# def dogs_create_view(request):
# 	form = Dogs_Forms(request.POST or None)
# 	if form.is_valid():
# 		form.save()

# 	context = {
# 		'form' : form
# 	}
# 	return render(request, "dogs/dogs_detail.html",context)
def dogs_detail_view(request):
	obj = Dogs.objects.get(id=1)
	context = {
		'object':obj
	}
	return render(request,"dogs/detail.html",context)