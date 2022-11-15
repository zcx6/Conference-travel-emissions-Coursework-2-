from pytest import raises
import pytest
from utils import *

class TestCity:
    def test_name_is_not_str(self):
        with raises(TypeError) as exception:
            zurich = City(111, 'Switzerland', 52, 47.22, 8.33)

    def test_country_is_not_str(self):
        with raises(TypeError) as exception:
            zurich = City('Zurich', 111, 52, 47.22, 8.33)

    def test_citizen_numbers_is_not_integer(self):
        #with raises(TypeError) as exception:
        north_pole =City('North Pole', 'Sweeden', 52, 90.0, 8.33)
            #zurich = City('Zurich', 'Switzerland', 52.8, 47.22, 8.33)

    def test_citizen_numbers_is_not_positive(self):
        with raises(ValueError) as exception:
            zurich = City('Zurich', 'Switzerland', -17, 47.22, 8.33)

    def test_latitude_is_not_float(self):
        with raises(TypeError) as exception:
            zurich = City('Zurich', 'Switzerland', 52, 47, 8.33)

    def test_latitude_is_invalid(self):
        with raises(ValueError) as exception:
            zurich = City('Zurich', 'Switzerland', 52, 100.8, 8.33)

    def test_longitude_is_not_float(self):
        with raises(TypeError) as exception:
            zurich = City('Zurich', 'Switzerland', 52, 47.22, 8)

    def test_longitude_is_invalid(self):
        with raises(ValueError) as exception:
            zurich = City('Zurich', 'Switzerland', 52, 47.22, 200.7)


    def test_distance_to(self):
        zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
        san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
        zrh_to_sfo = zurich.distance_to(san_francisco)

        assert zrh_to_sfo == 9374.70692719961


    def test_co2_to_fly_long_haul(self):
        zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
        san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
        zrh_to_sfo_co2 = zurich.co2_to(san_francisco)
        assert zrh_to_sfo_co2 == 146245428.0643139

    def test_co2_to_fly_short_haul(self):
        milan = City('Milan', 'Italy', 13, 45.4668, 9.1905)
        santander = City('Santander', 'Spain', 2, 43.462041, -3.809972)
        mil_to_san_co2 = milan.co2_to(santander)
        assert mil_to_san_co2 == 3426275.3967686924

    def test_co2_to_public_transport(self):
        kanazawa = City('Kanazawa', 'Japan', 10, 36.56, 136.66)
        seoul = City('Seoul', 'South Korea', 234, 37.57, 126.98)
        kan_to_seo_co2 = kanazawa.co2_to(seoul)
        assert kan_to_seo_co2 == 1731604.6249346354


class TestCityCollection:
    def test_countires(self):
        kanazawa = City('Kanazawa', 'Japan', 10, 36.56, 136.66)
        seoul = City('Seoul', 'South Korea', 234, 37.57, 126.98)
        zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
        san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
        tokai = City('Tokai', 'Japan', 1, 35.04, 136.91)






    if __name__ == "__main__":
        pytest.main()