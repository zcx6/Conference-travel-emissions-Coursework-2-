from typing import Dict, List, Tuple
import math

class City:
    def __init__(self, name, country, citizen_numbers, latitude, longitude):

        if name == '' or not isinstance(name, str):
            raise ValueError('name is not string')
        if country == '' or not isinstance(country, str):
            raise ValueError('country is not string')
        if not isinstance(citizen_numbers, int):
            raise ValueError('citizen_numbers is not integer ')
        if not int(citizen_numbers) > 0:
            raise ValueError('citizen_numbers is not positive')

        if not isinstance(latitude, float):
            raise ValueError('latitude is not decimal numbers')
        if not (-90 < float(latitude) < 90):
            raise ValueError('latitude is not restricted to the -90 to 90')
        if not isinstance(longitude, float):
            raise ValueError('longitude is not decimal numbers')
        if not (-180 < float(longitude) < 180):
            raise ValueError('longitude is not restricted to the -180 to 180')

        self.name = name
        self.country = country
        self.citizen_numbers = citizen_numbers
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other: 'City') -> float:
        R = 6371
        phi1 = self.latitude
        phi2 = other.latitude
        lamda1 = self.longitude
        lamda2 = other.longitude

        dLat = math.radians(phi2 - phi1)
        dLon = math.radians(lamda2 - lamda1)
        phi1 = math.radians(phi1)
        phi2 = math.radians(phi2)

        d = 2*R*math.asin(math.sqrt((math.sin(dLat/2))**2 + math.cos(phi1) * math.cos(phi2) * (math.sin(dLon/2))**2))
        return d


    def co2_to(self, other: 'City') -> float:
        d = self.distance_to(other)
        people = self.citizen_numbers
        if d <= 1000:
            return 200*d*people
        elif 1000 < d < 8000:
            return 250*d*people
        else:
            return 300*d*people




class CityCollection:

    def __init__(self, cities: 'City'):
        self.cities = cities

    def countries(self) -> List[str]:

        countries =[]
        for city in self.cities:
            countries.append(city.country)
        uniquecountry = list(set(countries))
        uniquecountry.sort(key=countries.index)
        return(uniquecountry)

    def total_attendees(self) -> int:
        attendees =[]
        for N in self.cities:
            attendees.append(N.citizen_numbers)

        total = sum(attendees)
        return total




    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError



