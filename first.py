# data =[movie_name,movie_url,img_url,movie_magnet,movie_info]
from bs4 import BeautifulSoup as bs4
import requests
import re
import os
def movie_name_search(movie_name):
    movie_name = movie_name.replace(' ','+')
    get = requests.get("https://www.imdb.com/find?s=tt&q="+movie_name+"&ref_=nv_sr_sm")
    bs = bs4(get.text,'html.parser')
    try:
        movie_name = bs.find("td",{"class":"result_text"}).find("a").text.strip()+" "+re.findall("\(\d+\)",bs.find("td",{"class":"result_text"}).text.strip())[0]
    except :
        return None
    if re.findall("\(\D+\)",bs.find("td",{"class":"result_text"}).text.strip())==[]:
        return movie_name
    else :
        return None

def movie_url_def(movie_name):
    movie_name =movie_name.replace(" ",'-')
    movie_name =movie_name.replace(":",'')
    movie_name =movie_name.replace(",",'-')
    movie_name =movie_name.replace("(",'')
    movie_name =movie_name.replace(")",'')
    movie_name =movie_name.replace(".",'')
    movie_name = movie_name.lower()
    return r"https://yts.lt/movie/"+movie_name

def movie_check(movie_url):
    get = requests.get(movie_url)
    bs = bs4(get.text,'html.parser')
    if bs.find("div",{"class":"col-xs-10 col-sm-14 col-md-7 col-lg-8 col-lg-offset-1"})==None:
        if __name__ == "__main__":
            movie_reminder(movie_url)
        else:
            return (None,None,None)
    else:
        return movie_dowload(movie_url,bs)

def movie_dowload(movie_url,bs):
    img_url= re.findall("src=.+jpg",str(bs.find("img",{"class":"img-responsive"})))[0]
    img_url = img_url[5:]
    movie_info=''
    for h in bs.find("div",{"class":"visible-xs col-xs-20"}).find_all("h2"):
        movie_info = movie_info+"\n"+h.text.strip()
    movie_magnet = {}
    for magnet in bs.find("p",{"class":"hidden-md hidden-lg"}).find_all("a"):
        m= re.findall("href=.+\" r",str(magnet))[0]
        movie_magnet[magnet.text.strip()]=m[6:-3]
    return (img_url,movie_magnet,movie_info)

def movie_reminder(movie_url):
    global movie_name
    w = open('reminder.txt' ,'a+')
    w.write("\n"+movie_url+'*'+movie_name)

def begin(movie_name):
    data=[]
    movie_name= movie_name_search(movie_name)
    if not movie_name==None :
        data.append(movie_name)
        movie_url= movie_url_def(movie_name)
        aa = movie_check(movie_url)
        data.append(movie_url)
        data.append(aa[0])
        data.append(aa[1])
        data.append(aa[2])
        return data
    else:
        return None