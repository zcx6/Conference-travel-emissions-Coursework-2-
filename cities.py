from typing import Dict, List, Tuple
import math

class City:
    def __init__(self, name, country, citizen_numbers, latitude, longitude):

        if name == '' or not isinstance(name, str):
            raise TypeError('name is not string')
        if country == '' or not isinstance(country, str):
            raise TypeError('country is not string')
        if not isinstance(citizen_numbers, int):
            raise TypeError('citizen_numbers is not integer ')
        if not int(citizen_numbers) > 0:
            raise ValueError('citizen_numbers is not positive')

        if not isinstance(latitude, float):
            raise TypeError('latitude is not decimal numbers')
        if not (-90 <= float(latitude) <= 90):
            raise ValueError('latitude is not restricted to the -90 to 90')
        if not isinstance(longitude, float):
            raise TypeError('longitude is not decimal numbers')
        if not (-180 <= float(longitude) <= 180):
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
        count = 0
        for city in self.cities:
            countries.append(city.country)
        unique_country = list(set(countries))
        unique_country.sort(key=countries.index)
        return(unique_country)

    def total_attendees(self) -> int:
        attendees = []
        for N in self.cities:
            attendees.append(N.citizen_numbers)
        total = sum(attendees)
        return total

    def total_distance_travel_to(self, city: City) -> float:
        tot_distance = 0
        for i in self.cities:
            tot_distance += i.distance_to(city) * i.citizen_numbers
        return tot_distance

    def travel_by_country(self, city: City) -> Dict[str, float]:
        dict = {}
        country = self.countries()
        for c in country:
            country_contain_cities = CityCollection([city for city in self.cities if city.country == c])
            dict[c] = country_contain_cities.total_distance_travel_to(city)
        return dict

    def total_co2(self, city: City) -> float:
        total = 0
        for i in self.cities:
            total += i.co2_to(city)
        return total

    def co2_by_country(self, city: City) -> Dict[str, float]:
        dict = {}
        country = self.countries()
        for c in country:
            country_contain_cities = CityCollection([city for city in self.cities if city.country == c])
            dict[c] = country_contain_cities.total_co2(city)
        return dict

    def summary(self, city: City):
        ZZZ = self.total_attendees() - city.citizen_numbers
        count = 0
        for i in self.cities:
            count += 1
        print('Host city:', city.name, '(', city.country, ')')
        print('Total CO2:', str(round((self.total_co2(city))/1000)), 'tonnes')
        print('Total attendees travelling to Zurich from', count-1, 'different cities:', ZZZ)

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        co2_emissions = []
        for c in self.cities:
            co2_emissions.append((c.name, self.total_co2(c)))
        sorted_co2_emissions = sorted(co2_emissions, key=lambda x: x[1])
        return sorted_co2_emissions

    def plot_top_emitters(self, city: City, n=10, save=False):
        a = self.co2_by_country(city)
        b = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
        x = list(b.keys())
        y = list(b.values())

        import matplotlib.pyplot as plt

        countries = x[0:n]
        values = y[0:n]
        countries.append('Everywhere else')
        other_country = sum(y[n:])
        values.append(other_country)

        fig = plt.figure(figsize=(12, 8))
        plt.bar(countries, values)
        plt.ylabel('Total emissions(kg CO2)')
        plt.title('Total emission from each country')
        plt.xticks(rotation=-15)
        plt.tick_params(axis='x', labelsize=8)

        if save==True:
            plt.savefig('{}.png'.format(city.name.lower().replace(' ', '_')))
        else:
            plt.show()









