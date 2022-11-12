import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import random,time
#create window
root=tk.Tk()
#init
width=500   #宽
height=600  #高
root.geometry(f"{width}x{height}")  #设置大小
root.resizable(False,False)    #禁止缩放窗口
root.config(bg="green")     #设置背景色
root.title("杨了个硕")


##start##
bg_img=Image.open("logo.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
#frames
frame0=tk.Frame(root,width=width,height=height,relief="flat",bg="white")
frame1=tk.Frame(root,width=width,height=height,relief="flat",bg="white")
frame0.place(x=0,y=0)
#back ground canvas init
bg_cv=tk.Canvas(frame0,width=width,height=height,relief="flat")#the canvas to show backgound image
bg_cv.place(x=0,y=0)
#put the background image onto the backgrond canvas
bg_cv.create_image(0,0,image=bg_img,anchor="nw")
#update
root.update()
time.sleep(2)


##main GUI##
root.update()

#about window
def show_about_window():
    about_win=tk.Toplevel(root,width=400,height=550)
    about_win.title("关于")
    about_win.resizable(False,False)

    text=tk.Text(about_win,font=("楷体",20))
    text.place(x=0,y=0,width=400,height=550)

    text.insert("0.0","游戏开发者&制作者:刘清硕\n版权所有:Light Bit Code(TM)")
    text.window_create("1.0")

    text.config(state="disabled")

#about
button_about=tk.Button(bg_cv,font=("楷书",30),text="关于我们",relief="flat",cursor="hand2",
                        command=show_about_window)
button_about.place(x=150,y=200,width=200,height=70)

root.mainloop()