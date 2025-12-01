import requests 

class DataManager:
    """
    Manages interactions with Google Sheets via the Sheety API.
    
    This class handles GET and POST requests to read from and write to
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

    def get_data(self)-> dict | None:
        """
        Retrieve data from the Google Sheet.
        
        Makes a GET request to the Sheety API and returns the sheet data
        as a Python dictionary.
        
        Returns:
            dict: The JSON response containing sheet data, or None if request fails.
        
        Raises:
            Prints error message to console if HTTPError or ConnectionError occurs.
        """

        try: 
            response = requests.get(url=self.url,headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data 
        except requests.exceptions.HTTPError as e:
            print(f"{e}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"{e}, connection refused.")
            return None

    def write_data(self,flight_details:dict)-> dict | None:
        """
        Add new data to the Google Sheet.
        
        Makes a POST request to the Sheety API to create a new row with
        the provided flight details.
        
        Args:
            flight_details (dict): A dictionary containing the flight data
                to be added to the sheet.
        
        Returns:
            dict: The JSON response from the API, or None if request fails.
        
        Raises:
            Prints error message to console if HTTPError or ConnectionError occurs.
        """
        
        try: 
            response = requests.post(url=self.url,headers=self.headers,json = flight_details)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"{e}, Please check the API key")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"{e}, connection refused.")
            return None