import os
import pandas
import sys
import googlemaps
from dotenv import load_dotenv


def main():

    load_dotenv()

    gmaps = googlemaps.Client(key=os.getenv('GMAPS_API_KEY'))
    file_path = sys.argv[1]
    origin_location = input("Enter origin location: ").replace(" ", "+")

    data = pandas.read_excel(file_path)

    for index, company in data.iterrows():
        print(index, company["Company Name"])


if __name__ == "__main__":
    main()
