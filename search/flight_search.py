import os 
from dotenv import load_dotenv
import requests

load_dotenv()

AMADEUS_ENDPOINT = os.getenv("AMADEUS_ENDPOINT")

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

    def _get_new_token(self)->str:
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

        response = requests.post(url=f"{AMADEUS_ENDPOINT}/v1/security/oauth2/token", headers=headers, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
    def get_IATA_code(self,city:str):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.

        Parameters:
        city (str): The name of the city for which to find the IATA code.

        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError, 
        or "Not Found" if no match is found due to a KeyError.
        
        The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
        name and other parameters to refine the search. It then attempts to extract the IATA code
        from the JSON response. 

        - If the city is not found in the response data (i.e., the data array is empty, leading to 
        an IndexError), it logs a message indicating that no airport code was found for the city and 
        returns "N/A".

        - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading 
        to a KeyError), it logs a message indicating that no airport code was found for the city 
        and returns "Not Found".
        """

        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        parameters = {
            "keyword" : city,
            "max": "2",
            "include" : "AIRPORTS",
        }

        response = requests.get(

            url=f"{AMADEUS_ENDPOINT}/v1/reference-data/locations/cities",
            params=parameters,
            headers=headers
        )
        #TODO add in try/except blocks for key errors when returning the response KeyErrors, IndexErrors 
        return response.json()["data"][0]["iataCode"]
