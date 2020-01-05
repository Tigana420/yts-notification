from datetime import date
import first
import pop_up
from tkinter import *
import wget
from PIL import ImageTk,Image
from os import system as sys
import time
text=''
f=open('yesterday.txt','r')
yesterday= f.read()
f.close()
today = str(date.today())

f = open('remind_later.txt','r')
remind_later=f.readlines()
f.close()

f = open('reminder.txt','a+')
for remind in remind_later:
    f.write(remind)
f.close()

f= open('remind_later.txt','w')
f.close()

f = open('reminder.txt','r')
movies=f.readlines()
f.close()
movies2=movies
if int(today[-2:])>int(yesterday[-2:]) or int(today[5:7])>int(yesterday[5:7]) or int(today[:4])>int(yesterday[:4]):
    for movie in movies:
        if not movie=='\n':
            num = movie.find('*')
            if not first.movie_check(movie[:num])==(None,None,None):
                data = first.begin(movie[num+1:-2])
                pop_up.begin(data)
            else:
                text=text+movie
    yesterday=open('yesterday.txt','w').write(today)
    f=open('reminder.txt','w').write(text)
    f.close()
