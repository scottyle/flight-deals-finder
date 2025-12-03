#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#Standard library imports 
from data.data_manager import DataManager
from search.flight_search import FlightSearch
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
            if flight_data["iataCode"] == "":
                flights = FlightSearch()
                iata_code = flights.get_IATA_code(city = flight_data["city"])
                data.update_data(id = flight_data["id"], iataCode= iata_code)
            else:
                pass #To be updated later. 
        breakpoint()
    else:
        print(f"Sheet_data returned back: {sheet_data}")
