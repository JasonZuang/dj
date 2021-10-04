from django.shortcuts import render

# Create your views here.
def list_detail_view(request):
	obj = list.objects.get(id=1)
	context = {
		"title": obj.title,
		"items": obj.items,
		"summary": obj.summary
	}
	return render(request, "list/detail.html",context)