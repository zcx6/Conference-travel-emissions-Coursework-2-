from utils import *

if __name__ == '__main__':
    file_path = Path("attendee_locations.csv")
    city_collection = read_attendees_file(file_path)

    zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)

