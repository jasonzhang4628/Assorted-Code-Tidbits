from bs4 import BeautifulSoup
import urllib.request
from bs4 import re

page = urllib.request.urlopen('http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp')

soup = BeautifulSoup(page)

print(soup)

items = soup.find_all('font')


print('BREAK')

for item in items:
    print(item)
    
food = re.findall(r'>[\w\s]*<',str(items)) #Looks for items between brackets
food_list = []

for item in food:
    item = item[1:len(item)-1]
    print(item)
    food_list.append(item)

food_list = food_list[12:]
print(food_list)
