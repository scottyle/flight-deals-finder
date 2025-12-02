import requests 

class DataManager:
    """
    Manages interactions with Google Sheets via the Sheety API.
    
    This class handles GET and PUT requests to read from and update to
    a Google Sheet through authenticated API calls.
    
    Attributes:
        api_key (str): Bearer token for API authentication.
        url (str): The Sheety API endpoint URL.
        headers (dict): HTTP headers including authorization for API requests.
    """

    def __init__(self,api_key,url) -> None:
        """
        Initialize the DataManager with API credentials.
        
        Args:
            api_key (str): The API key/bearer token for authentication.
            url (str): The full Sheety API endpoint URL.
        """

        self.api_key = api_key
        self.url = url
        self.headers = {

            "Content-type" : "application/json",
            "Authorization" : f"Bearer {self.api_key}"

        }

    def get_data(self)-> list | None:
        """
        Retrieve data from the Google Sheet.
        
        Makes a GET request to the Sheety API and returns the sheet data
        as a Python list.
        
        Returns:
            list: The JSON response containing sheet data, or None if request fails.
        
        Raises:
            Prints error message to console if HTTPError or ConnectionError occurs.
        """

        try: 
            response = requests.get(url=self.url,headers=self.headers)
            response.raise_for_status()
            try:
                data = response.json()["prices"]
                return data
            except KeyError as e:
                print(f"KeyError: {e} missing key value 'prices' in response.json()")
                return None
        except requests.exceptions.HTTPError as e:
            print(f"{e}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"{e}, connection refused.")
            return None

    def update_data(self,id:int,iataCode:str) -> dict | None:
        """
        Updates data from the Google Sheet.
        
        Makes a PUT request to the Sheety API
        
        Args:
            id: The ID of the row on the google sheet. 
            iataCode: The iataCode of the location. 

        Returns:
            list: The JSON response containing sheet data, or None if request fails.
        
        Raises:
            Prints error message to console if HTTPError or ConnectionError occurs.
        """    


        flight_details = {
            "price": {

                "iataCode" : iataCode

            }
        }
        try: 
            response = requests.put(url=f"{self.url}/{id}",headers=self.headers,json = flight_details)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"{e}, Please check the API key")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"{e}, connection refused.")
            return None