travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgard"]
    }
]

def add_new_country(country, visits, cities):
    new_dict = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
