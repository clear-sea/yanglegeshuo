import tkinter as tk
from tkinter import messagebox
import random,time

root=tk.Tk()
#init
width=500   #宽
height=600  #高
root.geometry(f"{width}x{height}")  #设置大小
root.resizable(False,False)    #禁止缩放窗口
root.config(bg="green")     #设置背景色

blankpos_global=0
colors=['gold','black','red','green','blue','yellow']   #colors

blank_list=[]#blank
#class

#卡片组类
class Group:
    def __init__(self,num,pos=(0,0)):
        global blankpos_global
        self.group=[]
        self.x,self.y=pos
        self.num=num
        for i in range(self.num):
            self.button=tk.Button(root,text=random.randint(1,10),bg='white',fg=random.choice(colors),font=("宋体",20),command=self.click)
            self.button.place(x=self.x,y=self.y,width=50,height=50)
            self.group.append(self.button)
            self.y+=25
            self.x=self.x+random.randint(2,15)-random.randint(2,15)

        for j in range(len(self.group)-1):
            self.group[j].config(state="disabled")
    
    def click(self):
        global blankpos_global,blank_list
        same_cards=0

        self.group[self.num-1].place(x=blankpos_global,y=550)
        self.group[self.num-1].config(state="disabled")
        self.group[self.num-2].config(state="normal")

        blank_list.append(self.group[self.num-1])
    
        blankpos_global+=50
        self.num-=1

        #delete cards in the blank
        for card0 in range(len(blank_list)):
            for card1 in range(card0,len(blank_list)):
                if(blank_list[card0]==blank_list[card1]):
                    same_cards+=1
                if(same_cards==3):
                    same_cards=0
        #exit
        if blankpos_global==500:
            ans=messagebox.askokcancel('信息','槽位已满,将退出')
            if ans:
                time.sleep(0.5)
                exit()

       
for n in range(random.randint(5,10)):
    x=random.randint(0,250)
    y=random.randint(50,350)
    num=random.randint(2,6)
    Group(num,pos=(x,y))
#mainloop
root.mainloop()