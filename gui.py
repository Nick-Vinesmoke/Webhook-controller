#Webhook-controller
#https://github.com/Nick-Vinesmoke/Webhook-controller
#https://github.com/Nick-Vinesmoke
#by Nick-Vinesmoke

from tkinter import *
import customtkinter as ct
from func import Func

class GUI:
    def __init__(self) -> None:
        self.win = ct.CTk()
        self.setTheme = ct.StringVar(value="dark")
        self.icon = "resources\\icon.ico"
        self.WinProperties()
        self.count = 100
        self.action = False
        self.Menu()
        


        self.win.mainloop()
    
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
        self.uperFame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030")
        self.uperFame.place(x=0, y=0)
        self.header = ct.CTkLabel(master=self.win, text="Webhook-Controller", font=('Arial Rounded MT bold', 30), bg_color='#303030', text_color='#14A5AE')
        self.header.place(x=100, y=15)
        self.addNew = ct.CTkButton(master=self.win, text="+", font=('Arial Rounded MT bold', 45), width=65, bg_color='#303030',border_color='#14A5AE',
                       command=lambda: [self.AddHook()])
        self.addNew.place(x=5, y=5)
        self.LoadHooks()
    
    def LoadHooks(self):
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
                            command=lambda current_url=self.url: [Func.ChooseHook(current_url.get("0.0", "end")),self.win.destroy(), GUI()], width=20, border_color="#50C878", hover_color='#50C878')

                self.url.insert("0.0", hooksList[i][1])
                self.url.configure(state="disabled")
                self.plate1.place(x=25, y=self.count)
                self.url.place(x=35, y=self.count + 45)
                self.title.place(x=35, y=self.count + 10)
                self.delete.place(x=380, y=self.count + 10)
                self.choose.place(x=280, y=self.count + 10)

                hooks.append(self.url)

                self.count = self.count + 150
    
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
                          command=lambda: [Func.AddHook(url.get()),self.win.destroy(), GUI(), url.destroy(),fame.destroy(), title.destroy(), close.destroy(),apply.destroy(),self.EndAction()],
                          border_color="#50C878", hover_color='#50C878')
        
            close = ct.CTkButton(master=self.win, text="⨉", font=('Arial Rounded MT bold', 18),width=35,height=30,corner_radius = 10, bg_color='#303030',
                          command=lambda: [fame.destroy(), title.destroy(), close.destroy(), url.destroy(), apply.destroy(), self.EndAction()],
                          border_color="#872D26", hover_color='#872D26')
            close.place(x=450, y=5)
            apply.place(x=450, y=35)
    def EndAction(self):
        self.action = False


if __name__ == "__main__":
    GUI()