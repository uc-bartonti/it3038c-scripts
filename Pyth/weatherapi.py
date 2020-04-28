import json
import requests

print('please enter your zip code:')
zip = input()

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=72132ab609191f93122aa378ab6bc13b' % zip)
data=r.json()
print(data['weather'][0]['description'])
