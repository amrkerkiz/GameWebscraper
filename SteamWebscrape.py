import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time


# This function goes to the url above, downloads the data, converts it and accesses the html part
def get_data(url):
    #Assigns the the request to get the url to r
    r = requests.get(url)
    # Takes the data from the request url page and loads it into a python dictionary
    data = dict(r.json())
    return data['results_html']


def parse(data):
    #Empty list for the dictionary at the end of function
    gameslist = []
    #Parses the data in html
    soup = BeautifulSoup(data, 'html.parser')
    #Each game cards begins with the 'a' tag
    games = soup.find_all('a')
    #Allows me to loop through
    for game in games:
        title = game.find('span', {'class': 'title'}).text
        price = game.find('div', {'class' : 'search_price'}).text.strip().split('$')[1]
        #If the try method isn't used it will not work because not all games have a discount price
        try:
            #Discount price of the game, is found using the same div 'search_price', but we need to break it up so both prices are displayed on one part of the list and other
            discprice = game.find('div', {'class' : 'search_price'}).text.strip().split('$')[2]
        except:
            discprice = 'no discount'

        #Creates a dictionary for the data collected above
        mygame ={
           'title': title,
           'price': price,
           'discprice': discprice,
       }
       #Will loop the dictionary above through the list
        gameslist.append(mygame)
    return gameslist

#Puts data into csv file
def output(results):
    gamesdf = pd.concat([pd.DataFrame(g) for g in results])
    gamesdf.to_csv('steamScraper.csv', index=False)
    print('Fin. Saved to CSV')
    print(gamesdf)
    return

results = []
for x in range(0, 200, 50):
    data = get_data(f'https://store.steampowered.com/search/results/?query&start={x}&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&os=win&infinite=1')
    results.append(parse(data))
    print('Results Scraped: ', x)
    time.sleep(1.5)

output(results)
