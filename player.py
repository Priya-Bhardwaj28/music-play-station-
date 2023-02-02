from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from pygame import mixer
import os
import time
import pygame 


w= tk.Tk()
w.title("Music Station")
w.geometry('736x440')
w.resizable(0,0)
w['bg']='#101010'

mixer.init()
index=0

#                       A D D            M U S I C                  F I L E 
def open_dir():
    global filename
    filename= tk.filedialog.askdirectory()
    os.chdir(filename)
    for j in os.listdir(filename):
        if j.endswith('.mp3'):
            song_list.insert(END,j)
        
           
  
def back():
    global index
    index-=1
    mixer.music.load(lst[index])
    mixer.music.play()

    e1['text']= 'Playing - '+ '\n' + lst[index]

def forw():
    global index
    index+=1
    mixer.music.load(lst[index])
    mixer.music.play()

    e1['text']= 'Playing - '+ '\n' + lst[index]

    
#                        A  L R E A  D Y        P R E S E N T    
def playing_current_songs(event):
    mixer.music.load(song_list.get(ACTIVE))
    mixer.music.play()
    mixer.music.unpause()
    e1['text']= 'Playing - '+ '\n' + song_list.get(ACTIVE)

def unpa():
    try :
        paused
    except :    
        try:
            mixer.music.load(song_list)
            e1['text']= 'Playing - '+ '\n' + song_list.get(ACTIVE)
            mixer.music.play()

            mixer.music.unpause()
        except:
            tk.messagebox.showwarning('MY MUSIC STATION','Unpause after playing.')
    else:
        e1['text']= 'Playing - '+ '\n' + song_list.get(ACTIVE)
        mixer.music.unpause()

def pau():
    global paused
    paused= True
    e1['text']= 'Pause - '+ '\n' + song_list.get(ACTIVE)
    mixer.music.pause()  


def set_vol(var):
    v= str(volume.get())
    get_vol.config(text=v)
    x= int(var)/100 
    mixer.music.set_volume(x)   # command

def About():
    messagebox.showinfo('MY MUSIC STATION',"THIS 'MY MUSIC STATION' is made by 'PRIYA BHARDWAJ'")
    
   
def save_memo_button():
    save=tk.filedialog.asksaveasfilename(initialfile='Untitled.txt', 
                                        defaultextension=".txt", 
                                        filetypes=[("All Files","*.*"), 
                                            ("Text Documents","*.txt")])
    f= open(save,'w')
    f.write(mem.get(1.0, END))
    
    f.close()


def music_s():
    pass   

def update_clock():
    now= time.strftime('%H:%H:%S')
    ck.configure(text=now)
    c.after(1000,update_clock)

w.iconbitmap('lg.ico')

c= tk.Canvas(w,width=732,height=435,bg='#101010')
c.place(x=0,y=0)


lb= tk.Label(c,text='My Music Station !',bg='#101010',fg='#D3D3D3',font=('Comic Sans MS bold',30))
lb.place(x=220,y=12)

lb= tk.Label(c,text='Lists of songs!',bg='#101010',fg='#D3D3D3',font=('Comic Sans MS bold',15))
lb.place(x=21,y=12)

#                                         S E A R C H 

ls=tk.Label(c,text='🎵',bg='#101010',fg='#D3D3D3',font=('chiller',50))
ls.place(x=200,y=100)


e1=tk.Label(c,text='Play Music ',bg='#101010',fg='#D3D3D3',font=('chiller',15))
e1.place(x=250,y=120,height=40,width=300)


#                                  L I S T   O F   S O N G S 


song_list= tk.Listbox(c, bg='#D3D3D3',fg='#101010',font=('Agency FB',13))
song_list.place(x=10,y=50 ,height=380,width= 180)

os.chdir("D:\songs\hollywood")
lst=os.listdir()

for i in lst:
    if i.endswith('.mp3'):
        song_list.insert(END,i) 
           

song_list.bind('<Double-1>',playing_current_songs)




scrollbar=tk.Scrollbar(w)
scrollbar.pack(side=tk.RIGHT,fill='y')
song_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=song_list.yview)


#                                        B U T T O N S 

backward= tk.Button(c,text='⏮',bg='#101010',fg='#D3D3D3',borderwidth=0 ,font=('cooper black',25),command=back)   
backward.place(x=260,y=170)   

unpause= tk.Button(c,text='⏸',bg='#101010',fg='#D3D3D3',borderwidth=0,font=('cooper black',25),command=unpa)   
unpause.place(x=330,y=170)

pause= tk.Button(c,text='▶',bg='#101010',fg='#D3D3D3',borderwidth=0,font=('cooper black',25),command=pau)   
pause.place(x=400,y=170)   


forward= tk.Button(c,text='⏭',bg='#101010',fg='#D3D3D3',borderwidth=0,font=('cooper black',25),command= forw)   
forward.place(x=470,y=170)         

vol_button= tk.Label(c,text='🔊',bg='#101010',fg='#D3D3D3',borderwidth=0,font=('cooper black',30))   
vol_button.place(x=626,y=57)             


#                                          M E M O

lb= tk.Label(c,text='Write Your Thought\'s !',bg='#101010',fg='#D3D3D3',font=('Comic Sans MS bold',15))
lb.place(x=220,y=250)


mem= tk.Text(c,bg='#D3D3D3',fg='#101010',font=('Comic Sans MS',15))
mem.place(x=220,y=290 ,height=117,width= 450)

quote='''Peace begins when expectation ends. 
'''
mem.insert(END,quote)

mem_save_button= tk.Button(c,text='Save',bg='#101010',fg='#D3D3D3',borderwidth=0, font=('Comic Sans MS',15),command= save_memo_button)
mem_save_button.place(x=600,y=410,height=25,width=70)

#                                                V O L U M E

volume= DoubleVar()

sc= tk.Scale(c,variable= volume,from_= 0,to=100,bg='#101010',fg='#D3D3D3',borderwidth=0,font=('Comic Sans MS',15),cursor= 'dot' ,showvalue= 0,orient= VERTICAL,width=3,highlightthickness=0,command=set_vol)
sc.set(17)
sc.place(x=690,y=100,height=327,width=70)


get_vol= tk.Label(c,bg='#101010',fg='#D3D3D3',font=('Comic Sans MS',15))
get_vol.place(x=666,y=67)

#                                               F I L E  B A R
m1= tk.Menubutton(c,text='File',bg='#101010',fg='#D3D3D3',borderwidth=0,font=('Comic Sans MS',20))
m1.place(x=640,y=10)
m1.menu= tk.Menu(m1,tearoff=0,bg='#101010',fg='#D3D3D3',borderwidth=0,font=('Comic Sans MS',10))
m1['menu']=m1.menu
m1.menu.add_command(label='Open',command=open_dir)
m1.menu.add_command(label='About',command= About)
m1.menu.add_command(label='Exit',command= w.destroy)


#                                M U S I C    S C A L E 
'''
mu= DoubleVar()

music_scale= tk.Scale(c,variable= mu,from_= 0,to=100,bg='#101010',fg='#D3D3D3',borderwidth=0,font=('Agency FB',15),cursor= 'dot' ,showvalue= 0,orient= HORIZONTAL,width=3,highlightthickness=0,command=music_s)
music_scale.set(17)
music_scale.place(x=200,y=190,height=70,width=370)
'''

#                                C L O C K


ck= tk.Label(c,bg='#101010',fg='#D3D3D3',font=('Comic Sans MS',20 ))
ck.place(x=350,y=60)
update_clock()






'''
im=Image.open('srch.png')
nw_img=im.resize((40,45))
photo= ImageTk.PhotoImage(nw_img)
song=StringVar()
ls=tk.Label(c,image=photo)
ls.place(x=210,y=100)

e1=tk.Entry(c,textvariable=song,bg='#101010',fg='#D3D3D3',font=('cooper black',20))
e1.place(x=250,y=100,height=40,width=300)'''
'''
m1= tk.Menubutton(c,text='Search',bg='#101010')
m1.place(x=10,y=13)
m1.menu= tk.Menu(m1,tearoff=0,bg='#101010',fg='#D3D3D3')
m1['menu']=m1.menu

m1= tk.Menubutton(c,text='Next',bg='#101010')
m1.place(x=100,y=13)
m1.menu= tk.Menu(m1,tearoff=0,bg='#101010',fg='#D3D3D3')
m1['menu']=m1.menu
'''



w.mainloop()