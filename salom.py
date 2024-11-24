import requests
import json


m=[]
p=0
f=[]
while p<=20:
   r = requests.get ( 'https://randomuser.me/api/')
   data=r.json()
   for i in data['results']:
      if i['gender']=='male':
         name=i['name']['first'] + ' '+ i['name']['last']
         if name not in m:
            m.append(name)
      if i['gender']=='female':
         name=i['name']['first'] + ' '+ i['name']['last']
         if name not in f:
            f.append(name)
   p+=1
print(f'There are female names: ')
print(f)
print('----------------------------------')
print(f'There are male names: ')
print(m)
