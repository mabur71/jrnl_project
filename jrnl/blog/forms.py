from django import forms
from .models import Records, Sites

class AddLogForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.site = kwargs.pop('site')
		self.id = kwargs.pop('id')
		super(AddLogForm, self).__init__(*args, **kwargs)
	text   = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
	person = forms.CharField(max_length = 20)
	def clean_text(self):
		text = self.cleaned_data['text']
		return text
	def clean_person(self):
		person = self.cleaned_data['person']
		return person
	def save(self):
		if self.id == '':
			site_obj = Sites.objects.get(name=self.site)
			record = Records()
			record.site = site_obj
			record.text = self.cleaned_data['text']
			record.person = self.cleaned_data['person']
		else:
			try:
				record = Records.objects.get(id=self.id)
			except Records.DoesNotExist:
				return ''
			record.text = self.cleaned_data['text']
			record.person = self.cleaned_data['person']
		
		record.save()
		return record
