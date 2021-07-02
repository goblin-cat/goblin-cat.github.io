# /hunter-comic/
import json
import os
from bs4 import BeautifulSoup
import lxml


## Main functions ##


ch3Files=os.listdir('ch3')
numPages = len(ch3Files)

for i in range(0,numPages):
    path='ch3//'+ch3Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    mylinks = soup.findAll('a')
    
    for i in range(0,len(mylinks)):
        if ("hunter" not in mylinks[i]["href"]):
            mylinks[i]["href"] = "/hunter-comic"+mylinks[i]["href"]
        else:
            print("skip")
 
    with open(path, "w") as ogfile:
       ogfile.write(str(soup))