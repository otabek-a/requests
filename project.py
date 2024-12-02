import os
import requests
TOKEN=os.getenv("TOKEN")
base=f"https://api.telegram.org/bot{TOKEN}"
chat_id=6723268646


message=requests.get(f'{base}/getUpdates')


natija=message.json()
last_message = natija 
print(last_message)
#r=requests.get(f"{base}/sendMessage?chat_id={chat_id}&text={last_text}")
#result=r.json()