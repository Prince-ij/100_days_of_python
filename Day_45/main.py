from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com")
contents = response.text

soup = BeautifulSoup(contents, 'lxml')

article_tags = soup.select('.titleline a')
article_texts = []
article_links = []
for article_tag in article_tags:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)
article_score = [int(score.getText().split()[0]) for score in soup.find_all(class_='score')]


max_index = article_score.index(max(article_score))

print(article_texts[max_index])
print(article_links[max_index])
print(article_score[max_index])
