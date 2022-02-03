import requests;
from bs4 import BeautifulSoup;

movieNumber=input('please enter the number of movies you want to search:')
url='https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count='+ movieNumber;

response=requests.get(url)
print('*'*45)
parseHtml=BeautifulSoup(response.content,'html.parser')
for movies in parseHtml.findAll('div',class_='lister-item mode-advanced'):
    print(movies.h3.a.text)
    print(movies.strong.text)
    print(movies.find('span',class_='genre').text.strip())
    print(movies.find('span',class_='lister-item-year').text.strip())
    print(f"https://www.imdb.com{movies.a.get('href')}")
    print('*'*45)
