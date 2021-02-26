import os
import pyautogui
import time
import keyboard

from tkinter import Tk, Label, Button

pyautogui.FAILSAFE = True



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Albion Item Seller")

        self.label = Label(master, text="DURDURMAK İÇİN MOUSE'U SAĞ ÜST KÖŞEYE GÖTÜR")
        self.label.pack()

        self.oto_button = Button(master, text="SELL ITEMS", command=self.oto)
        self.oto_button.pack()

    def oto(self):
        print("başladı")
        time.sleep(5)
        a = 1
        while a == 1: 
            pyautogui.click(x=1285, y=425)
            time.sleep(0.25)
            pyautogui.click(x=829, y=515)
            time.sleep(0.25)
            pyautogui.click(x=829, y=637)
            pyautogui.click(x=829, y=637)
            time.sleep(0.25)
            pyautogui.click(x=1144, y=731)
            time.sleep(0.5)    

        

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()