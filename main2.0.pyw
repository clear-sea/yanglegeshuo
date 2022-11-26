import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import random,time

#init
width=500   #宽
height=600  #高

root=tk.Tk()
root.geometry(f"{width}x{height}")
root.resizable(False,False)
#globals
all_cards_list=[]
all_cards_num=0

blank=[0,0,0,0,0,0,0,0,0,0]
blank_pos=0
blank_num=0
id=0
##class Card##
class Card:
    def __init__(self,pos,id):
        self.x,self.y=pos
        self.id=id
        self.data=random.randint(1,10)
        self.body=tk.Button(frame1,text=self.data,bg="white",fg="green",font=("宋体",25),activebackground="white",activeforeground="green",command=self.move)
        self.body.place(x=self.x,y=self.y,width=50,height=50)

    def move(self):
        global blank,blank_pos,blank_num
        if blank_num==10:
            messagebox.showinfo("提醒","槽位已满<Faild>")
        else:
            blank[blank_num]=self

            self.body.place(x=blank_pos,y=550)
                    
            self.body.config(state="disabled")
            blank_pos+=50
            blank_num+=1

            cnt=0
            delete_cards_list=[0,0,0]
            a=0
            for card in blank:
                if (not isinstance(card,int)) and card.data==self.data:
                    cnt+=1
                    delete_cards_list[a]=card
                    a+=1
                    if cnt==3:
                        cnt=0
                        a=0
                        
                        delete_cards_list[0].delete()
                        delete_cards_list[1].delete()
                        delete_cards_list[2].delete()


    def delete(self):
        global blank,blank_pos,blank_num,all_cards_list

        self.body.destroy()
        blank_num-=1
        blank_pos-=50
        blank[blank_num]=0
        all_cards_list[self.id]=0
 
##start##
bg_img=Image.open("images/logo.png")#open the background image
bg_img=ImageTk.PhotoImage(bg_img)#cast to TK image
#frames
frame0=tk.Frame(root,width=width,height=height,relief="flat",bg="white")
frame1=tk.Frame(root,width=width,height=height,relief="flat",bg="green")
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
    about_frame=tk.Frame(root,width=500,height=600,bg="white")
    frame0.place_forget()
    about_frame.place(x=0,y=0)

    text=tk.Text(about_frame,font=("楷体",20))
    text.place(x=0,y=50,width=500,height=600)

    text.insert("0.0","游戏开发者&制作者:刘清硕\n版权所有:Light Bit Code(TM)")

    def exit_about():
        about_frame.place_forget()
        frame0.place(x=0,y=0)

    exit_btn=tk.Button(about_frame,text="<",relief="flat",command=exit_about)
    exit_btn.place(x=0,y=0,width=50,height=50)

    text.config(state="disabled")

def start_main_game():
    global id,all_cards_list,all_cards_num

    frame0.place_forget()
    frame1.place(x=0,y=0)

    def exit_about():
        frame1.place_forget()
        frame0.place(x=0,y=0)

    exit_btn=tk.Button(frame1,text="<",relief="flat",command=exit_about)
    exit_btn.place(x=0,y=0,width=50,height=50)

    for i in range(random.randint(7,9)):
        for j in range(3):
            all_cards_num+=1
            card=Card((random.randint(0,450),random.randint(50,500)),id)
            id+=1
            all_cards_list.append(card)



#about
button_about=tk.Button(bg_cv,font=("楷书",30),text="关于我们",relief="flat",cursor="hand2",
                        command=show_about_window)
button_about.place(x=150,y=200,width=200,height=70)

button_about=tk.Button(bg_cv,font=("楷书",30),text="开始",relief="flat",cursor="hand2",
                        command=start_main_game)
button_about.place(x=150,y=300,width=200,height=70)

root.mainloop()