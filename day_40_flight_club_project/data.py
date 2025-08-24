import requests
from config import *
class Data:
    def __init__(self):
        pass

    def init_with_iata(self):
        """
        Initialize the sheets with the iata codes
        """
        sheet_data = requests.get(SHEETY_ENDPOINT, headers=sheety_header).json()
        for i in range(0, 9):
            city = sheet_data['sheet1'][i]['city']
            get_city_param = {
                "keyword": city.upper()
            }

            iata_codes = requests.get(IATA_ENDPOINT, params=get_city_param, headers=amadeus_header).json()
            print(iata_codes)

            iata_input = {
                "sheet1": {
                    "iataCode": iata_codes['data'][0]['iataCode']
                }
            }

            response = requests.put(f"{SHEETY_ENDPOINT}/{i+2}", json=iata_input, headers=sheety_header)
            print(response.text)

    def get_lowest_price(self):
        """
        Get a price lower than the current price, from today to 6 months from now
        """
        sheet_data = requests.get(SHEETY_ENDPOINT, headers=sheety_header).json()
        for i in range(8):
            iata_code = sheet_data['sheet1'][i]['iataCode']
            get_flight_param = {
                "originLocationCode": "ABV",
                "destinationLocationCode": iata_code,
                "departureDate": "2024-12-19",
                "returnDate": "2025-03-20",
                "adults": 1
            }

            response = requests.get(AMADEUS_FLIGHT_OFFERS, params=get_flight_param, headers=amadeus_header)
            flight_data = response.json()

            lowest_price = sheet_data['sheet1'][i]['lowestPrice']
            price = flight_data['data'][0]['price']['total']
            origin = f"Nigeria {flight_data['data'][0]['itineraries'][0]['segments'][0]['departure']['iataCode']}"
            destination = sheet_data['sheet1'][i]['city']
            departure_date = flight_data['data'][0]['itineraries'][0]['segments'][0]['departure']['at']
            return_date = flight_data['data'][0]['itineraries'][0]['segments'][0]['arrival']['at']


            messages = []

            if float(price) < float(lowest_price):
                message = f"Low Price alert!\n\
                    only ${price} to fly from {origin} to {destination}, \
                        from {departure_date} to {return_date}"
                messages.append(message)
                return messages
        messages = ["No low price found"]
        return messages

    def post_customer(self, name, email):
        """
        Post the customer data to the sheety api
        return all the emails in the sheet
        """
        customer_input = {
            "sheet1": {
                "name": name,
                "email": email
            }
        }

        response = requests.post(SHEETY_CUSTOMER_ENDPOINT, json=customer_input, headers=sheety_header)
        print(response.text)

    def get_emails(self):
        cutomer = requests.get(SHEETY_CUSTOMER_ENDPOINT, headers=sheety_header).json()
        customer_emails = [customer['email'] for customer in cutomer['sheet1']]
        return customer_emails
