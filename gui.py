import first
from tkinter import *
import first
import wget
import pop_up
from PIL import ImageTk,Image
from os import system as sys
#print(first.begin('tranformers '))
spam={}
def movie_delete(i):
    global spam
    global frame2
    f=open('reminder.txt','r')
    movies  = f.readlines()
    f.close()
    x=-1
    text=''
    for movie in movies:
        x+=1
        if x==i:
            pass
        else :
            text = text + movie
    f=open('reminder.txt','w')
    f.write(text)
    f.close()
    spam={}
    frame2.place_forget()
    movies_text()

def arrange_movie(movie,i):
    global frame2
    global spam
    spam[i]=[]
    spam[i].append(LabelFrame(frame2))
    spam[i].append(Label(spam[i][0],text=movie))
    spam[i].append(Button(spam[i][0],text='X',command= lambda : movie_delete(i)))
    spam[i][0].pack(fill="x")
    spam[i][1].pack(side='left')
    spam[i][2].pack(side='right')


def movies_text():
    global frame2
    try:
        frame2.place_forget()
    except :
        pass
    f=open('reminder.txt','r')
    movies  = f.readlines()
    i=-1
    frame2 = LabelFrame(root)
    frame2.place(relwidth=1,relheight=0.85,rely=0.15)
    for movie in movies:
        if not movie=='\n' and not movie =='':
            movie=movie.replace('\n','')
            dig=movie.find('*')
            i+=1
            arrange_movie(movie[dig+1:],i)
    f.close()

def set_reminder(data):
    f=open('reminder.txt','a+')
    f.write(data[1]+'*'+data[0]+'\n')
    f.close()
    movies_text()
    notfi_button.place_forget()
    notfi_ok.place_forget()

def searchh(mv_s):
    global notfi_button
    global notfi_ok
    try:
        notfi_button.place_forget()
    except :
        pass
    if not str(mv_s) == 'None'and not str(mv_s)=='' :
        data =first.begin(mv_s)
        if data == None:
            notfi_button= Label(frame1,text='No result.')
            notfi_button.place(relheight=0.45,rely=0.55)
        else:
            if data[3]==None:
                notfi_button= Label(frame1,text='No torrent ..')
                notfi_button.place(relheight=0.45,rely=0.55)
                notfi_ok = Button(frame1,text='set a reminder',command= lambda : set_reminder(data))
                notfi_ok.place(rely=0.60,relx=0.2)
            else :
                pop_up.begin(data)
                
                
    else: pass

root =Tk()
movie_to_search=''
xx = Canvas(root , height = 500, width = 350)
frame1 = LabelFrame(root )
input = Entry(frame1)
search_button = Button(frame1 ,text='go!',command = lambda :searchh(input.get()))
movies_text()


frame1.place(relwidth=1,relheight=0.15,rely=0)
input.place(relwidth=0.7,relheight=0.5,relx=0,rely=0.05)
search_button.place(relwidth=0.2,relheight=0.5,rely=0.05,relx=0.75)

xx.pack()





root.mainloop()
