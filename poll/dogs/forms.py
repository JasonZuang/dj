from django import forms
from .models import Dogs 

class Dogs_Forms(forms.ModelForm):
	class Meta:
		model = Dogs
		fields = [
			'breed',
			'name'
		]

class Raw_Dogs_Form(forms.Form):
	breed = forms.CharField()
	name = forms.CharField()
	