from cities import City, CityCollection
from pathlib import Path
import csv

def read_attendees_file(filepath: Path) -> CityCollection:
    with open('attendee_locations.csv') as f:
        f_csv=csv.reader(f)
        headers=next(f_csv)

        list_of_city=[]
        for row in f_csv:
            city=City(row[1], row[3], int(row[0]), row[4], row[5])
            list_of_city.append(city)

        city_collection = CityCollection(list_of_city)
        return city_collection

            #print(row[1])