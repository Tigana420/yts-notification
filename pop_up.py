from tkinter import *
import wget
from PIL import ImageTk,Image
from os import system as sys
# data =[movie_name,movie_url,img_url,movie_magnet,movie_info]
def get_magnet(k):
    pass

def xxx(i,k,v):
    spam[i]=[]
    spam[i].append(v)
    spam[i].append(Button(movie_data,text=k,command= lambda : get_magnet(spam[i][0])))
    spam[i][1].pack()

def quit_(data):
    f=open('remind_later.txt','a+')
    f.write(data[1]+'*'+data[0]+'\n')
    f.close()
    root.destroy()




def get_data(data):
    global spam
    global movie_data
    spam={}
    text = data[0]+'\n'+data[4]
    i=0
    text_pack = Label(movie_data,text=text)
    text_pack.pack()
    for k,v in data[3].items():
        i+=1
        xxx(i,k,v)
    remind_me=Button(movie_data,text='Remind me later',command= lambda : quit_(data))
    remind_me.pack(fill='x')

#data=['The Sublet (2015)', 'https://yts.lt/movie/the-sublet-2015', 'https://img.yts.lt/assets/images/movies/the_sublet_2015/medium-cover.jpg', {'720p.BluRay': 'https://yts.lt/torrent/download/1D15B8CE5CA939B299C3977F0B406988A2C4D51F', '1080p.BluRay': 'https://yts.lt/torrent/download/DA69B5D74083DF10067FDD430C4C06C13F370BC3'}, '\n2015\nDrama / Horror / Mystery / Thriller']
def begin(data):
    global movie_data
    global root
    global img_lab
    global img
    root =Tk()
    root.geometry("400x350")
    labl=LabelFrame(root)
    labl.place(relwidth=1,relheight=1)
    image_url= data[2]#ektb l url t3 l taswira
    file_name = wget.download(image_url)
    sys('ren '+r'medium-cover.jpg '+r'medium-cover.png')
    img=ImageTk.PhotoImage(Image.open('medium-cover.png'),master=labl)
    img_lab = Label(labl,image=img) 
    sys(r'del medium-cover.png')
    movie_data = Label(labl)
    get_data(data)
    movie_data.pack(side='right',expand='y')
    img_lab.pack(side='right',expand='y')
    root.mainloop()