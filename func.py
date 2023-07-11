#Webhook-controller
#https://github.com/Nick-Vinesmoke/Webhook-controller
#https://github.com/Nick-Vinesmoke
#by Nick-Vinesmoke

import os
from file import File
from encryption import Crypt
import requests
import json

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
        if hooksList != 'null':
            for i in range(len(hooksList)):
                hooksList[i] = hooksList[i].split("[/hook/%context%/]")
            key = Func.GetKey()
            for i in range(len(hooksList)):
                hooksList[i][1]= Crypt.Decrypt(hooksList[i][1],key)
            return hooksList
        return 'null'
    
    def DelHook(url):
        str_url = str(url)
        str_url = str_url.replace('\n','')
        dataList = Func.GetHooks()
        key = Func.GetKey()
        string= ''
        for x in range(len(dataList)):
            print(dataList[x][1]+'?='+str_url)
            if dataList[x][1] != str_url:
                print(dataList[x][1]+'!='+str_url)
                enc_url = Crypt.Encrypt(dataList[x][1],key)
                string +='[/bin/%context%/]'+dataList[x][0]+"[/hook/%context%/]"+enc_url.decode("ascii")
        File.Write(string, "data\\hooks", True)
    
    def Send(url,context,file_paths):
        payload = {
            'content': context
        }
        response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

        if response.status_code == 204:
            print('Message and files sent successfully.')
        else:
            print('Error sending message and files:', response.text)

        for file in file_paths:
            with open(file, 'rb') as file:
                files = {'file': file}
                response = requests.post(url, files=files)
        
            if response.status_code == 200:
                print('File sent successfully.')
            else:
                print('Error sending file:', response.text)

        
