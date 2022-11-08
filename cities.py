from typing import Dict, List, Tuple

class City:
    def __init__(self, name, country, citizen_numbers, latitude, longitude):

        self.name=name
        self.country=country
        self.citizen_numbers=citizen_numbers
        self.latitude=latitude
        self.longitude=longitude

    def numberofcitizens(self):
        pass


    # def restrictedforcoordinates(self):
    #     for latitudes in self.latitude:
    #         if -90 < latitudes < 90:


    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError

class CityCollection:

    def __init__(self, cities: 'City'):
        self.cities = cities

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        #for city in self.cities:
        pass



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

