# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = 	False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.utils import IntegrityError
import json

class Concerts(models.Model):
	concert_id = models.AutoField(primary_key=True)
	band = models.ForeignKey('Bands', models.DO_NOTHING)
	place = models.ForeignKey('Places', models.DO_NOTHING)
	org = models.ForeignKey('Organizers', models.DO_NOTHING)
	date = models.DateField()
	price = models.FloatField()
	description = models.TextField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'concerts'


	def load_from_json(self):
		with open('concerts/concerts.json', 'r') as f:
			obj = json.load(f)
			Concerts.objects.all().delete()
			Bands.objects.all().delete()
			Places.objects.all().delete()
			Organizers.objects.all().delete()
			for c in obj:
				self.add_row(c)

	def add_row(self, row):
		b = Bands(b_name= row['band']['b_name'], country = row['band']['country'], albums_num = row['band']['albums_num'])
		b.save()
	
		pl = Places(pl_name= row['place']['pl_name'], city = row['place']['city'], capacity = row['place']['capacity'])
		pl.save()
			
		org = Organizers(org_name= row['organizer']['org_name'], commercial = row['organizer']['commercial'])
		org.save()
	
		if not Concerts.objects.all().filter(band_id=b.band_id, place_id=pl.place_id, org_id=org.org_id):
 			self = Concerts(band_id=b.band_id, place_id=pl.place_id, org_id=org.org_id, date=row['date'], price=row['price'], description=row['description'])
 			self.save()		


	def __str__(self):
		tupl = (self.concert_id, Bands.objects.get(pk = self.band_id), Places.objects.get(pk = self.place_id), 
			Organizers.objects.get(pk = self.org_id), self.price, self.date, self.description)
		return "{'id':%s, 'band':%s, 'place':%s, 'org':%s, 'price':%s, 'date':%s, 'description':%s} " % tupl


class Bands(models.Model):
	band_id = models.AutoField(primary_key=True)
	b_name = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	albums_num = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'bands'

	def __str__(self):
		return "{'band_id': %s, 'b_name': %s, 'country': %s, 'albums_num': %s}" % (self.band_id, self.b_name, self.country, self.albums_num)


class Organizers(models.Model):
	org_id = models.AutoField(primary_key=True)
	org_name = models.CharField(max_length=45)
	commercial = models.BooleanField()

	class Meta:
		managed = False
		db_table = 'organizers'

	def __str__(self):
		return "{'org_id': %s, 'org_name': %s, 'commercial': %s}" % (self.org_id, self.org_name, self.commercial)


class Places(models.Model):
	place_id = models.AutoField(primary_key=True)
	pl_name = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	capacity = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'places'

	def __str__(self):
		return "{'place_id': %s, 'pl_name': %s, 'city': %s, 'capacity': %s}" % (self.place_id, self.pl_name, self.city, self.capacity)
