import urllib
import requests
import json
myinput= input('What do you want to search for? : ')
url = 'https://www.europeana.eu/api/entities/suggest?wskey=apidemo&text=' + str(myinput)
response = requests.get(url).json()
mylist = response['items']

for i in mylist:
    print(i)

