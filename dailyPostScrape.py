import requests
from bs4 import BeautifulSoup
import time

def news_scrape():
    source = requests.get('https://dailypost.ng/').text
    soup = BeautifulSoup(source, 'lxml')

    parent_div = soup.find_all('a')
    news_file = open('DailyPost.txt', 'a')
    for news in parent_div:
        try:
            news_link = news['href']
            news_headlines = news.h2.text
            date_posted = news.find('span', class_='mvp-cd-date left relative').text
        except AttributeError:
            pass
        else:
            '''print(date_posted)
            print(news_link)
            print(news_headlines)
            print()'''
            news_file.write(date_posted + '\n')
            news_file.write(news_link + '\n')
            news_file.write(news_headlines + '\n')
            news_file.write('\n\n')

while True:
    news_scrape()
    time.sleep(7200)