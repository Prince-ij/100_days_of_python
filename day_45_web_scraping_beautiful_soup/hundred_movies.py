import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, 'lxml')

movies = soup.find_all(name='h3', class_='title')

movie_list = []
for movie in movies:
    movie_list.append(movie.getText())

movie_list.reverse()

for movie in movie_list:
    with open('top_100_movies.txt', 'a', encoding='utf-8') as file:
        file.write(f'{movie}\n')
