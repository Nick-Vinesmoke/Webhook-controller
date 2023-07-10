import os
from file import File
from encryption import Crypt
import requests

class Func:
    def AddHook(url):
        str_url = str(url)
        if not str_url.find("https://discord.com/api/webhooks/"):
            if not os.path.exists("data\\hooks"):
                File.Write('create',"data\\hooks")
            try:
                webhook_name = Func.get_webhook_name(str_url)
            except:
                webhook_name = 'error'
            key = Func.GetKey()
            enc_url = Crypt.Encrypt(str_url,key)
            data = webhook_name+'[/hook/%context%/]'+enc_url.decode("ascii")
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
    
    def GetHooks():
        hooksList = File.Read("data\\hooks")
        for i in range(len(hooksList)):
            hooksList[i] = hooksList[i].split("[/hook/%context%/]")
        key = Func.GetKey()
        for i in range(len(hooksList)):
            hooksList[i][1]= Crypt.Decrypt(hooksList[i][1],key)
        return hooksList
    
    def DelHook(url):
            str_url = str(url)
            str_url = str_url.replace('\n','')
            try:
                webhook_name = Func.get_webhook_name(str_url)
            except:
                webhook_name = 'error'
            webhook_name = '[/bin/%context%/]'+webhook_name+'[/hook/%context%/]'
            with open("data\\hooks", 'rb') as file:
                fileContent = file.read()
            fileContent = fileContent.decode("ascii")
            index = fileContent.find(webhook_name)
            index += len(webhook_name)
            endIndex = fileContent.find("[/bin/%context%/]",index)
            for i in range(index, endIndex):
                webhook_name+= fileContent[i]
            fileContent = fileContent.replace(webhook_name,"")
            File.Write(fileContent, "data\\hooks", True)

