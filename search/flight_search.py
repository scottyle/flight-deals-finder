import os 
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN_ENDPOINT = os.getenv("TOKEN_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        
        """
        Initialize an instance of the FlightSearch class.
        This constructor performs the following tasks:

        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.

        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token() method.

        """

        self._api_key = os.getenv("AMADEUS_API_KEY"),
        self._api_secret = os.getenv("AMADEUS_API_SECRET"),
        self._token = self._get_new_token()
        
    
    def get_IATA_code(self,city):
        return "TESTING"
    
    def _get_new_token(self):
        """

        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.

        Returns:
            str: The new access token obtained from the API response.
        """

        headers = {
            "Content-Type" : "application/x-www-form-urlencoded" 
        }

        body = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']