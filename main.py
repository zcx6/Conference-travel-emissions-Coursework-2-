from utils import *

if __name__ == '__main__':
    file_path = Path("attendee_locations.csv")
    city_collection = read_attendees_file(file_path)

    zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
    san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)

    # zrh_to_sfo = zurich.distance_to(san_francisco)
    # print(zrh_to_sfo)
    #
    # zrh_to_sfo_co2 = zurich.co2_to(san_francisco)
    # print(zrh_to_sfo_co2)

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


    # kanazawa = City('Kanazawa', 'Japan', 10, 36.56, 136.66)
    # seoul = City('Seoul', 'South Korea', 234, 37.57, 126.98)
    # kan_to_seo = kanazawa.distance_to(seoul)
    # print(kan_to_seo)
    # kan_to_seo_co2 = kanazawa.co2_to(seoul)
    # print(kan_to_seo_co2)

    kanazawa = City('Kanazawa', 'Japan', 10, 36.56, 136.66)
    seoul = City('Seoul', 'South Korea', 234, 37.57, 126.98)
    san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
    tokai = City('Tokai', 'Japan', 1, 35.04, 136.91)
    city_collection = CityCollection([kanazawa, seoul, san_francisco, tokai])
    sorted_by_emission = city_collection.sorted_by_emissions()
    print(sorted_by_emission)



