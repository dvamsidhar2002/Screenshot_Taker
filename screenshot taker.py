import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Screenshot Taker')

canvas1 = tk.Canvas(root,width=300,height=300)
canvas1.pack()

def ScreenShot():
    sc=pyautogui.screenshot()
    sc.save('G:\PyCharm Projects II\SS_py.png')

myButton = tk.Button(text='Take Screenshot',command=ScreenShot,bg='black',fg='yellow',font=15)
canvas1.create_window(150,150,window=myButton)


root.mainloop()