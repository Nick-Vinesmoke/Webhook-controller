#Webhook-controller
#https://github.com/Nick-Vinesmoke/Webhook-controller
#https://github.com/Nick-Vinesmoke
#by Nick-Vinesmoke

from tkinter import *
import customtkinter as ct
from func import Func
from tkinter import filedialog

class GUI:
    def __init__(self) -> None:
        self.win = ct.CTk()
        self.setTheme = ct.StringVar(value="dark")
        self.icon = "resources\\icon.ico"
        self.WinProperties()
        self.count = 100
        self.action = False
        self.change = 0
        self.Menu()
        print(self.webhooks)
        self.win.bind("<MouseWheel>", self.mouse_wheel)
        self.win.mainloop()
    
    def mouse_wheel(self, event):
        self.count = 100
        if event.num == 5 or event.delta == -120:
            self.change += 50
        if event.num == 4 or event.delta == 120:
            self.change -= 50
        if self.count+self.change <= 100:
            for i in range(len(self.webhooks)):
                self.webhooks[i][0].place(x=25, y=self.count+self.change)
                self.webhooks[i][2].place(x=35, y=self.count + 45+self.change)
                self.webhooks[i][1].place(x=35, y=self.count + 10+self.change)
                self.webhooks[i][3].place(x=380, y=self.count + 10+self.change)
                self.webhooks[i][4].place(x=280, y=self.count + 10+self.change)
                self.count = self.count + 150

    
    def WinProperties(self):
        self.win.geometry("500x600+560+240")  
        self.win.minsize(500,300)
        self.win.title("Webhook-Controller") 
        self.win.resizable(False, False)  
        self.win.configure(fg_color="#242424")
        self.win.iconbitmap(self.icon)  
        ct.set_appearance_mode('dark')
        ct.set_default_color_theme('green')

    def Menu(self):
        self.LoadHooks()
        self.uperFame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030")
        self.uperFame.place(x=0, y=0)
        self.header = ct.CTkLabel(master=self.win, text="Webhook-Controller", font=('Arial Rounded MT bold', 30), bg_color='#303030', text_color='#14A5AE')
        self.header.place(x=100, y=15)
        self.addNew = ct.CTkButton(master=self.win, text="+", font=('Arial Rounded MT bold', 45), width=65, bg_color='#303030',border_color='#14A5AE',
                       command=lambda: [self.AddHook()])
        self.addNew.place(x=5, y=5)
    
    def LoadHooks(self):
        hooksList = Func.GetHooks()
        if hooksList!= 'null':
            hooks = []
            self.webhooks = []
            for i in range(len(hooksList)):
                self.webhook = []
                self.webhook.append(ct.CTkFrame(master=self.win, width=450, height=120, fg_color="#303030", border_color="#14A5AE", border_width=2))
                self.webhook.append(ct.CTkLabel(master=self.win, text=hooksList[i][0], font=('Arial Rounded MT bold', 24), bg_color='#303030', text_color='#14A5AE'))
                self.webhook.append(ct.CTkTextbox(master=self.win, width=430, height=65, fg_color="#404040", bg_color='#303030'))
                self.webhook.append(ct.CTkButton(master=self.win, text="delete", font=('Arial Rounded MT bold', 18), width=30, bg_color='#303030',
                              command=lambda current_url=self.webhook[2]: [Func.DelHook(current_url.get("0.0", "end")),self.win.destroy(), GUI()], 
                              border_color="#872D26", hover_color='#872D26'))
                self.webhook.append(ct.CTkButton(master=self.win, text="choose", font=('Arial Rounded MT bold', 18), bg_color='#303030',
                            command=lambda current_url=self.webhook[2]: [self.ChooseHook(current_url.get("0.0", "end"))], width=20, border_color="#50C878", hover_color='#50C878'))

                self.webhook[2].insert("0.0", hooksList[i][1])
                self.webhook[2].configure(state="disabled")
                self.webhook[0].place(x=25, y=self.count)
                self.webhook[2].place(x=35, y=self.count + 45)
                self.webhook[1].place(x=35, y=self.count + 10)
                self.webhook[3].place(x=380, y=self.count + 10)
                self.webhook[4].place(x=280, y=self.count + 10)
                self.count = self.count + 150

                self.webhooks.append(self.webhook)
                hooks.append(self.webhook[2])
                
        '''
        hooksList = Func.GetHooks()
        if hooksList!= 'null':
            hooks = []
            for i in range(len(hooksList)):
                self.plate1 = ct.CTkFrame(master=self.win, width=450, height=120, fg_color="#303030", border_color="#14A5AE", border_width=2)
                self.title = ct.CTkLabel(master=self.win, text=hooksList[i][0], font=('Arial Rounded MT bold', 24), bg_color='#303030', text_color='#14A5AE')
                self.url = ct.CTkTextbox(master=self.win, width=430, height=65, fg_color="#404040", bg_color='#303030')
                self.delete = ct.CTkButton(master=self.win, text="delete", font=('Arial Rounded MT bold', 18), width=30, bg_color='#303030',
                              command=lambda current_url=self.url: [Func.DelHook(current_url.get("0.0", "end")),self.win.destroy(), GUI()], 
                              border_color="#872D26", hover_color='#872D26')
                self.choose = ct.CTkButton(master=self.win, text="choose", font=('Arial Rounded MT bold', 18), bg_color='#303030',
                            command=lambda current_url=self.url: [self.ChooseHook(current_url.get("0.0", "end"))], width=20, border_color="#50C878", hover_color='#50C878')

                self.url.insert("0.0", hooksList[i][1])
                self.url.configure(state="disabled")
                self.plate1.place(x=25, y=self.count)
                self.url.place(x=35, y=self.count + 45)
                self.title.place(x=35, y=self.count + 10)
                self.delete.place(x=380, y=self.count + 10)
                self.choose.place(x=280, y=self.count + 10)

                hooks.append(self.url)

                self.count = self.count + 150
                '''


    def ChooseHook(self,url):
        print(url)
        self.files_list =[]
        self.files = ct.StringVar(value="files")
        str_url = str(url)
        str_url = str_url.replace('\n','')
        name = Func.get_webhook_name(str_url)
        plate = ct.CTkFrame(master=self.win, width=500, height=600, fg_color="#242424")
        plate.place(x=0, y=0)
        uperFame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030")
        uperFame.place(x=0, y=0)
        middleFame = ct.CTkFrame(master=self.win, width=500, height=450, fg_color="#303030")
        middleFame.place(x=0, y=100)
        header = ct.CTkLabel(master=self.win, text=name, font=('Arial Rounded MT bold', 34), bg_color='#303030', text_color='#14A5AE')
        header.place(relx=0.5, y=30, anchor=CENTER)
        self.text = ct.CTkTextbox(master=self.win, width=460, height=360, fg_color="#404040", bg_color='#303030', border_color="#14A5AE", border_width=2)
        self.text.place(x=20, y=120)
        send= ct.CTkButton(master=self.win, text="send", font=('Arial Rounded MT bold', 24), bg_color='#242424',
                            command=lambda: [Func.Send(str_url,self.text.get("0.0", "end"),self.files_list),self.CleanFiles()], width=20, border_color="#50C878", hover_color='#50C878')
        
        addFile= ct.CTkButton(master=self.win, text="Add file", font=('Arial Rounded MT bold', 18), bg_color='#303030',
                            command=lambda: [self.LoadFile()], width=20, border_color="#14A5AE", hover_color='#303030',corner_radius=8)
        
        files = ct.CTkLabel(master=self.win, textvariable = self.files ,width=400, bg_color='#303030', fg_color="#262626",font=('Arial Rounded MT bold', 18),anchor = 'w', corner_radius=6)

        close = ct.CTkButton(master=self.win, text="⨉", font=('Arial Rounded MT bold', 18),width=25,height=30,corner_radius = 10, bg_color='#303030',
                          command=lambda: [plate.destroy(), close.destroy(),uperFame.destroy(),header.destroy(),middleFame.destroy(),self.text.destroy(),send.destroy(),addFile.destroy(),files.destroy()],
                          border_color="#872D26", hover_color='#872D26')
        close.place(x=450, y=5)
        addFile.place(x=5, y=503)
        files.place(x=93, y=505)
        send.place(x=205, y=557)
    

    def CleanFiles(self):
        self.files_list =[]
        self.files.set("files")
        self.text.insert("0.0", " ")
        fame = ct.CTkFrame(master=self.win, width=300, height=100, fg_color="#303030", bg_color='#404040',corner_radius=30,border_color="#14A5AE", border_width=2)
        fame.place(relx=0.5,rely=0.5, anchor=CENTER)
        header = ct.CTkLabel(master=self.win, text="message sent", font=('Arial Rounded MT bold', 34), bg_color='#303030', text_color='#14A5AE')
        header.place(relx=0.5, y=280, anchor=CENTER)
        ok = ct.CTkButton(master=self.win, text="OK", font=('Arial Rounded MT bold', 24), bg_color='#303030',
                            command=lambda: [fame.destroy(),header.destroy(),ok.destroy()], width=20, border_color="#50C878", hover_color='#50C878')
        ok.place(relx=0.5, y=325, anchor=CENTER)

    def LoadFile(self):
        filepaths = filedialog.askopenfilenames(title="choose file")
        listpaths = list(filepaths)
        self.files_list = list(self.files_list+listpaths)

        fileNames = ''
        for files in self.files_list:
            index = files.rfind("/")
            files = files[index+1:]
            fileNames = fileNames+files+', '

        if self.files.get() == 'files':
            self.files.set('')
        if len(self.files.get()+fileNames) > 40:
            string = self.files.get()+fileNames
            self.files.set(string[:40])
        else:
            self.files.set(self.files.get()+fileNames)
        
        print(self.files_list)
        print(self.files.get())

        

    def AddHook(self):
        if not self.action:
            self.action = True
            fame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030",border_color='#14A5AE',border_width=2)
            fame.place(x=0, y=0)
            title = ct.CTkLabel(master=self.win, text="Add new Webhook", font=('Arial Rounded MT bold', 24), bg_color='#303030', text_color='#14A5AE')
            title.place(x=11, y=5)
            url = ct.CTkEntry(master=self.win, width=400, bg_color='#303030', fg_color="#262626",font=('Arial Rounded MT bold', 18), placeholder_text="WebHook URL")
            url.place(x=10, y=35)
            apply = ct.CTkButton(master=self.win, text="⩗", font=('Arial Rounded MT bold', 18),width=35,height=30,corner_radius = 10, bg_color='#303030',
                          command=lambda: [Func.AddHook(url.get()),self.win.destroy(), GUI()],
                          border_color="#50C878", hover_color='#50C878')
        
            close = ct.CTkButton(master=self.win, text="⨉", font=('Arial Rounded MT bold', 18),width=35,height=30,corner_radius = 10, bg_color='#303030',
                          command=lambda: [fame.destroy(), title.destroy(), close.destroy(), url.destroy(), apply.destroy(), self.EndAction()],
                          border_color="#872D26", hover_color='#872D26')
            close.place(x=450, y=5)
            apply.place(x=450, y=35)
    def EndAction(self):
        self.action = False