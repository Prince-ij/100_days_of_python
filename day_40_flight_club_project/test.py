import requests

def get_access_token(client_id, client_secret, auth_url):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(auth_url, data=payload)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        response.raise_for_status()

# Example usage
client_id = 'IfImG6G19eD0jFrwnoJADu0WH9yvwUUz'
client_secret = 'Gjf1B6J3H17CetJT'
auth_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'

access_token = get_access_token(client_id, client_secret, auth_url)
print(f'Access Token: {access_token}')
# from config import *
# sheet_data = requests.get(SHEETY_ENDPOINT, headers=sheety_header).json()

# iata_code = sheet_data['sheet1'][0]['iataCode']
# get_flight_param = {
#     "originLocationCode": "ABV",
#     "destinationLocationCode": iata_code,
#     "departureDate": "2024-12-19",
#     "returnDate": "2025-03-20",
#     "adults": 1
# }

# response = requests.get(AMADEUS_FLIGHT_OFFERS, params=get_flight_param, headers=amadeus_header)
# flight_data = response.json()
# print(flight_data['data'][0]['itineraries'][0]['segments'][0]['departure']['iataCode'])
