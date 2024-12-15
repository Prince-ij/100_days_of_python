weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

def to_f(c):
    return c * 9 / 5 + 32

weather_f = {name: to_f(temp) for (name, temp) in weather_c.items()}

print(weather_f)
