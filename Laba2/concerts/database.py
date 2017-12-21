from django.db import connection
from collections import namedtuple
import json

class Database:

	def __init__(self):
		self.cursor = None

	def connect(self):
		self.cursor = connection.cursor()

	def load_from_json(self):
		with open('concerts/concerts.json', 'r') as f:
			obj = json.load(f)
			for c in obj:
				self.add_row(c)

	def add_row(self, row):
		self.cursor.execute("INSERT INTO bands VALUES (NULL, %s,%s,%s);",
				[row['band']['name'], row['band']['country'], row['band']['albums_num']])

		self.cursor.execute("INSERT INTO places VALUES (NULL, %s,%s,%s);",
				[row['place']['name'], row['place']['city'], row['place']['capacity']])

		self.cursor.execute("INSERT INTO organizers VALUES (NULL, %s,%s);",
					[row['organizer']['name'], row['organizer']['commercial']])

		self.cursor.execute("INSERT INTO concerts VALUES (NULL, (SELECT band_id from bands where name = %s), "
								"(SELECT place_id from places where name = %s), (SELECT org_id from organizers where name = %s), %s, %s )",
			[ row['band']['name'], row['place']['name'], row['organizer']['name'], row['date'], row['price']])


	def get_concerts(self):
		#self.cursor.execute("SELECT bands.name, places.name, places.city, organizers.name, price, date from concerts, bands, places, orginizers "
		#					"WHERE band_id = bands.id and place_id = places.id and org_id = orginizers.id")


	def fetchall(self):
		desc = self.cursor.description
		nt_result = namedtuple('Result', [col[0] for col in desc])
		return [nt_result(*row) for row in self.cursor.fetchall()]