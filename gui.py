#Webhook-controller
#https://github.com/Nick-Vinesmoke/Webhook-controller
#https://github.com/Nick-Vinesmoke
#by Nick-Vinesmoke

from tkinter import *
import customtkinter as ct

class GUI:
    def __init__(self) -> None:
        self.win = ct.CTk()
        self.setTheme = ct.StringVar(value="dark")
        self.icon = "resources\\icon.ico"
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
        fame = ct.CTkFrame(master=self.win, width=500, height=70, fg_color="#303030",border_color='#14A5AE')


if __name__ == "__main__":
    GUI()