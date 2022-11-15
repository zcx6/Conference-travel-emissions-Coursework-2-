from cities import City, CityCollection
from pathlib import Path
import csv


def read_attendees_file(filepath: Path) -> CityCollection:
    with open('attendee_locations.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)

        list_of_city = []
        for row in f_csv:
            city = City(row[3], row[1], int(row[0]), float(row[4]), float(row[5]))
            list_of_city.append(city)
        city_collection = CityCollection(list_of_city)
        return city_collection


# N = City('North Pole', 'Sweeden', 52, 90.0, 8.33)
# print(N.latitude)