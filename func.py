import os
from file import File

class Func:
    def AddHook(url):
        if not os.path.exists("data\\hooks"):
            File.Write('create',"data\\hooks")
