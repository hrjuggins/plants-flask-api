import requests
import re
import json
from bs4 import BeautifulSoup

allLinks = {}
database = {}

def getAllPlantsLinks():
  URL = 'https://www.houseplantsexpert.com/a-z-list-of-house-plants.html'
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, 'html.parser')

  links = soup.findAll('a', {'data-name': True})
  pics = soup.findAll('img', {'class': 'imagePlant'})

  for i in range(0, 114):
    database[links[i]['data-name']] = {
                                        'href': links[i]['href'],
                                        'picture': pics[i]['src']
                                      }

getAllPlantsLinks()

def getPlantInfo(url):
  page = requests.get(url)

  soup = BeautifulSoup(page.content, 'html.parser')

  description = soup.find('p', {'class': 'lead-section'}).getText()
  rows = soup.findAll('tr')
  data = {
    'Description': description
  }
  for row in rows:
    col1 = row.findAll('td')[0].getText().strip()
    if "Humidity" in col1:
      col1 = "Humidity:"
    col2 = row.findAll('td')[1].getText().strip()
    data[col1] = col2
  return data

for key in database:
  print(database[key]['href'])
  database[key].update(getPlantInfo(database[key]['href']))

with open('data.txt', 'w') as json_file:
  json.dump(database, json_file)

  

