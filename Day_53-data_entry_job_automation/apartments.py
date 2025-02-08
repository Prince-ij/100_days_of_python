from bs4 import BeautifulSoup
import lxml
import requests


class RentApartments:
    def __init__(self, url, header):
        self.url = url
        self.header = header
        self.response = requests.get(url=self.url, headers=self.header)

        self.soup = BeautifulSoup(self.response.text, 'lxml')


    def get_address(self):
        address = []

        for addr in self.soup.find_all(attrs={'data-test': 'property-card-addr'}):
            address.append(addr.getText())

        return address


    def get_prices(self):
        prices = []

        for price in self.soup.find_all(attrs={'data-test': 'property-card-price'}):
            prices.append(price.getText().split('+')[0].split('/')[0])

        return prices


    def get_links(self):
        links = []

        for link in self.soup.find_all(attrs={'data-test': 'property-card-link'}):
            current_link = link.get('href')
            if not current_link.startswith('https://www.zillow.com'):
                current_link = f'https://www.zillow.com{current_link}'
            links.append(current_link)

        return links
