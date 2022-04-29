from tkinter import messagebox
import pyautogui
from tkinter import *
import webbrowser

try:
    # Close the splash screen.
    import pyi_splash
    pyi_splash.close()
except ImportError:
    # Otherwise do nothing.
    pass
    
root = Tk()

root.title("Auto Clicker BETA") #name of window
root.resizable(False, False) #Cant resize window
root.geometry("200x200")

new = 1
url = "https://github.com/NotsoFrostyy"

def openweb():
    webbrowser.open(url,new=new)

def click():
    messagebox.showwarning("Caution", "Auto Clicker will stop after 20 clicks")
    x = 0
    while x != 20:
        pyautogui.leftClick()
        x += 1
    if x == 20:
        messagebox.showinfo("Autoclicker", "Autoclicker reached 20 clicks")

button1 = Button(root, text="Start Clicking", width=10, height=1,
                 font=("helvetica", 12, "bold"), command=click, relief=GROOVE)
 
button1.place(x=50, y=50)

Btn = Button(text = "GITHUB",command=openweb,bg="Grey", fg="white",width=7, height=1, font=("helvetica", 10, "bold"), relief=GROOVE)
Btn.place(x=50,y=100)
btn2 = Button(width=4, height=1, font=("helvetica", 10, "bold"), text="Exit",bg='grey', fg='white', relief=GROOVE, command=root.destroy)
btn2.place(x=118, y=100)
 
root.mainloop()