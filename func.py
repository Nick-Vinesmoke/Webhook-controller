import os
from file import File
from encryption import Crypt
import requests

class Func:
    def AddHook(url):
        str_url = str(url)
        if str_url.find("https://discord.com/api/webhooks/"):
            if not os.path.exists("data\\hooks"):
                File.Write('create',"data\\hooks")
            webhook_name = Func.get_webhook_name(str_url)
            key = Func.GetKey()
            enc_url = Crypt.Encrypt(str_url,key)
            data = webhook_name+'[/hook/%context%/]'+enc_url
            File.Add(data,"data\\hooks")
        else:
            print("not a webhook")
        
    def GetKey():
        keyList = File.Read("data\\key.db")
        key = Crypt.Decrypt64(keyList[0])
        return key

    def get_webhook_name(webhook_url):
        response = requests.get(webhook_url)
        if response.status_code == 200:
            data = response.json()
            return data.get('name', 'Webhook Name Not Found')
        else:
            return 'Error'