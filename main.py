from utils import *

if __name__ == '__main__':
    file_path = Path("attendee_locations.csv")
    city_collection = read_attendees_file(file_path)

    zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
    san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)

    zrh_to_sfo = zurich.distance_to(san_francisco)
    print(zrh_to_sfo)

    zrh_to_sfo_co2 = zurich.co2_to(san_francisco)
    print(zrh_to_sfo_co2)

    # a = city_collection.countries()
    # print(a)
    #
    # b = city_collection.total_attendees()
    # print(b)
    #
    # c = city_collection.total_distance_travel_to(san_francisco)
    # print(c)
    #
    # d = city_collection.travel_by_country(zurich)
    # print(d)
    #
    # e = city_collection.total_co2(zurich)
    # print(e)
    #
    # f = city_collection.co2_by_country(zurich)
    # print(f)
    #
    # city_collection.summary(zurich)
    #
    # h = city_collection.sorted_by_emissions()
    # print(h)
    #
    # city_collection.plot_top_emitters(zurich, 10, False)

