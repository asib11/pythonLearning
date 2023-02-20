import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(response.text, 'html.parser')
article = soup.find_all('article')


with open('data.csv','w') as file:
    csv_write =writer(file)
    csv_write.writerow(['title','url','date'])
    for i in article:
        tag = i.find('a')
        title = tag.get_text()
        url = tag['href']
        date = i.find('time')['datetime']
        csv_write.writerow([title,url,date])
    print('done scrap')
