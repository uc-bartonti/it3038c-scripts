import json
import requests


r = requests.get('http://localhost:3000')
data=r.json()
for line in data: 
    print("{0} is {1}".format(line['name'],line['color']))