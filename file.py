#Webhook-controller
#https://github.com/Nick-Vinesmoke/Webhook-controller
#https://github.com/Nick-Vinesmoke
#by Nick-Vinesmoke

class File:
    def Write (contexts,FILENAME, ready = False):
        with open(FILENAME, 'wb') as file:
            if isinstance(contexts, str):
                if contexts != "create":
                    if not ready:
                        file.write(bytes('[/bin/%context%/]'+contexts, "UTF-8"))
                    else:
                        file.write(bytes(contexts, "UTF-8"))
            else:
                for context in contexts:
                    file.write(bytes('[/bin/%context%/]'+context, "UTF-8"))

    def Add(context,FILENAME):
        with open(FILENAME, 'ab') as file:
            file.write(bytes('[/bin/%context%/]'+context, "UTF-8"))
    
    def Read(FILENAME):
        try:
            with open(FILENAME, 'rb') as file:
                data = file.read()
                data = data.decode("utf-8")
                list = data.split("[/bin/%context%/]")
                try:
                    list.remove('')
                except:
                    pass
                return list
        except:
            return "null"