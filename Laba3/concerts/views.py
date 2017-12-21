from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import connection
from collections import namedtuple
from concerts.models import Concerts, Bands, Places, Organizers 
from .forms import BandForm, ConcertForm, OrganizerForm, PlaceForm

# Create your views here.

def load(request):
	c = Concerts()
	c.load_from_json()
	return HttpResponseRedirect(reverse('concerts:index'))


def index(request):
	concerts = Concerts.objects.all();
	curs = connection.cursor();
	if request.method == "POST":
		data = request.POST  
		if not (data['comm'] == ""):
			concerts = concerts.filter(org__in=Organizers.objects.all().filter(commercial=data['comm']))
		if not ((data['bdate'] == "") and (data['tdate'] == "")):
			concerts = concerts.filter(date__range=(data['bdate'], data['tdate']))
		if not (data['word'] == ""):
			concerts = concerts.filter(description__iregex=data['word'])
		return render(request, 'concerts/base.html', {'concerts': concerts})
	else:
		return render(request, 'concerts/base.html', {'concerts': concerts}) 
	

def remove(request, concert_id):
	if request.method == "POST":
		Concerts.objects.get(pk = concert_id).delete()		 
	return HttpResponseRedirect(reverse('concerts:index'))


def detail(request, concert_id):
	if request.method == "POST":
		return HttpResponseRedirect(reverse('concerts:index'))
	else:
		concert = Concerts.objects.get(pk=concert_id)
		return render(request, 'concerts/detail.html', {'concert': concert})


def edit(request, concert_id):
	concert = get_object_or_404(Concerts, pk = concert_id)
	band = Bands.objects.get(pk = concert.band_id)
	place = Places.objects.get(pk = concert.place_id)
	org = Organizers.objects.get(pk = concert.place_id)
	if request.method == "POST":
		b_form = BandForm(request.POST, instance=band)
		pl_form = PlaceForm(request.POST, instance=place)
		org_form = OrganizerForm(request.POST, instance=org)
		con_form = ConcertForm(request.POST, instance=concert)
		
		concert.date=con_form['date'].value() 
		concert.price=con_form['price'].value()
		concert.description=con_form['description'].value()
		concert.save()
		band.b_name=b_form['b_name'].value()
		band.country=b_form['country'].value()
		band.albums_num=b_form['albums_num'].value()
		band.save()
		place.pl_name=pl_form['pl_name'].value()
		place.city=pl_form['city'].value()
		place.capacity=pl_form['capacity'].value()
		place.save()
		org.org_name=org_form['org_name'].value()
		org.commercial=org_form['commercial'].value()
		org.save()

		return HttpResponseRedirect(reverse('concerts:index'))
	else:
		con_form = ConcertForm(instance=concert)
		b_form = BandForm(instance=band)
		pl_form = PlaceForm(instance=place)
		org_form = OrganizerForm(instance=org)
	return render(request, 'concerts/edit.html', {'concert_id':concert_id, 'con_form':con_form, 'b_form':b_form,
													'pl_form':pl_form, 'org_form':org_form})


def create(request):
	if request.method == "POST":
		b_form = BandForm(request.POST)
		pl_form = PlaceForm(request.POST)
		org_form = OrganizerForm(request.POST)
		con_form = ConcertForm(request.POST)
		
		row = {'date': con_form['date'].value(),
				'price': con_form['price'].value(),
				'band': {'b_name': b_form['b_name'].value(), 
						'country': b_form['country'].value(),
						'albums_num': b_form['albums_num'].value()},
				'place': {'pl_name': pl_form['pl_name'].value(),
						'city': pl_form['city'].value(),
						'capacity': pl_form['capacity'].value()},
				'organizer': {'org_name': org_form['org_name'].value(),
							'commercial': org_form['commercial'].value()},
				'description': con_form['description'].value(),
				}
		c = Concerts()
		c.add_row(row)
		return HttpResponseRedirect(reverse('concerts:index'))
	else:
		con_form = ConcertForm()
		b_form = BandForm()
		pl_form = PlaceForm()
		org_form = OrganizerForm()
	return render(request, 'concerts/create.html', {'con_form':con_form, 'b_form':b_form, 'pl_form':pl_form, 'org_form':org_form})


def logs(request):
	curs = connection.cursor()
	curs.execute("select * from logs")
	logs = fetchall(curs)
	return render(request, 'concerts/logs.html', {'logs':logs})



def fetchall(curs):
		desc = curs.description
		nt_result = namedtuple('Result', [col[0] for col in desc])
		return [nt_result(*row) for row in curs.fetchall()]