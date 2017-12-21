from django import forms
from .models import Concerts, Bands, Places, Organizers

class BandForm(forms.ModelForm):
	class Meta:
		model = Bands
		fields = ( 'b_name', 'country', 'albums_num')
		labels = { 'b_name': 'Name',
				'albums_num':'Albums numbers'}  

class ConcertForm(forms.ModelForm):
	class Meta:
		model = Concerts
		fields = ('price', 'date', 'description')


class OrganizerForm(forms.ModelForm):
	class Meta:
		model = Organizers
		fields = ( 'org_name', 'commercial',)
		labels = { 'org_name': 'Name',
				'commercial':'Is commercial'}


class PlaceForm(forms.ModelForm):
	class Meta:
		model = Places
		fields = ( 'pl_name', 'city', 'capacity',)
		labels = { 'pl_name': 'Name',
				'capacity':'Place capacity'}
