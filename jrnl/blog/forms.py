from django import forms
from .models import Records, Sites

class AddLogForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.site = kwargs.pop('site')
		super(AddLogForm, self).__init__(*args, **kwargs)
	text   = forms.CharField(widget=forms.Textarea)
	person = forms.CharField(max_length = 20)
	def clean_text(self):
		text = self.cleaned_data['text']
		return text
	def clean_person(self):
		person = self_cleaned_data['person']
		return person
	def save(self):
		site_obj = Sites.objects.get(name=self.site)
		record = Records()
		record.site = site_obj
		record.text = self.cleaned_data['text']
		record.person = self.cleaned_data['person']
		record.save()
		return record
