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
        self.action = False
        self.WinProperties()
        self.Menu()


        self.win.mainloop()
    
    def WinProperties(self):
        self.win.geometry("500x600+560+240")  # place and scale
        self.win.minsize(500,300)
        self.win.title("Webhook-Controller")  # name of the window
        self.win.resizable(False, False)  # deformation of the window
        self.win.iconbitmap(self.icon)  # icon
        ct.set_appearance_mode('dark')
        ct.set_default_color_theme('green')

    def Menu(self):
        uperFame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030")
        uperFame.place(x=0, y=0)
        header = ct.CTkLabel(master=self.win, text="Webhook-Controller", font=('Arial Rounded MT bold', 30), bg_color='#303030', text_color='#14A5AE')
        header.place(x=100, y=15)
        addNew = ct.CTkButton(master=self.win, text="+", font=('Arial Rounded MT bold', 45), width=65, bg_color='#303030',border_color='#14A5AE',
                       command=lambda: [self.AddHook()])
        addNew.place(x=5, y=5)
    
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
                          command=lambda: [fame.destroy(), title.destroy(), close.destroy(), url.destroy(),apply.destroy(),self.EndAction()],
                          border_color="#50C878", hover_color='#50C878')
        
            close = ct.CTkButton(master=self.win, text="⨉", font=('Arial Rounded MT bold', 18),width=35,height=30,corner_radius = 10, bg_color='#303030',
                          command=lambda: [fame.destroy(), title.destroy(), close.destroy(), url.destroy(), apply.destroy(), self.EndAction(), Func.AddHook(url.get())],
                          border_color="#872D26", hover_color='#872D26')
            close.place(x=450, y=5)
            apply.place(x=450, y=35)
    def EndAction(self):
        self.action = False

if __name__ == "__main__":
    GUI()