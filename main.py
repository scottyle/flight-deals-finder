#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#Standard library imports 
from data.data_manager import *
from search.flight_search import *
import os 

#Third-party imports 
from dotenv import load_dotenv

load_dotenv()

SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")
SHEETY_URL = os.getenv("SHEETY_URL")

if __name__ == "__main__":

    data = DataManager(api_key=SHEETY_API_KEY,url=SHEETY_URL)

    sheet_data = data.get_data()
    if sheet_data:
        for flight_data in sheet_data:
            try:
                if flight_data["iataCode"] == "":
                    flights = FlightSearch(flight_data["city"])
                    iata_code = flights.get_IATA_code()
                else:
                    print("iataCode exists")
            except KeyError as e:
                print(f"KeyError: {e} missing iataCode key.")
            flight_data.update({"iataCode":iata_code})

        #Loop through sheet_data again, to make a PUT request to update the Google Sheet with IATA codes
        for flight_data in sheet_data:
            data.update_data(id = flight_data["id"], iataCode= flight_data["iataCode"])
            
    else:
        print(f"Sheet_data returned back: {sheet_data}")