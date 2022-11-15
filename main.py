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
    d = city_collection.travel_by_country(zurich)
    print(d)
    #
    # e = city_collection.total_co2(zurich)
    # print(e)
    #
    # f = city_collection.co2_by_country(zurich)
    # print(f)
    #
    # city_collection.summary(zurich)
    #
    h = city_collection.sorted_by_emissions()
    print(h)
    #
    # city_collection.plot_top_emitters(zurich, 10, False)

    # milan = City('Milan', 'Italy', 13, 45.4668, 9.1905)
    # santander = City('Santander', 'Spain', 2, 43.462041, -3.809972)
    # mil_to_san = milan.distance_to(santander)
    # print(mil_to_san)
    # mil_to_san_co2 = milan.co2_to(santander)
    # print(mil_to_san_co2)
    #
    #
    # kanazawa = City('Kanazawa', 'Japan', 10, 36.56, 136.66)
    # seoul = City('Seoul', 'South Korea', 234, 37.57, 126.98)
    # kan_to_seo = kanazawa.distance_to(seoul)
    # print(kan_to_seo)
    # kan_to_seo_co2 = kanazawa.co2_to(seoul)
    # print(kan_to_seo_co2)
    #
    #
