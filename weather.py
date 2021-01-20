import requests
import json
x='Live weather details'
print(x.center(50))
print(50*'-')
print(50*'-')
location=input("Enter your location : ")

url='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=8ee0c75a91f50a95bd4418f59f8e0f76'%(location)
response=requests.get(url)
x=json.loads(response.text)

print('---------------------------------------------')
print('\ncurrent location : %s'%(location))
print('your coordinate ------> %s'%(x['coord']))
print('country ----> %s'%(x['sys']['country']))
print('weather ----> %s' %(x['weather'][0]['description']))
print('wind ---- > %s'%(x['wind']))
print('temperature ---> %s'%(x['main']['temp']))
print('\n---------------------------------------------')

