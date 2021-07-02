# /hunter-comic/
import json
import os
from bs4 import BeautifulSoup
import lxml


## Main functions ##


ch5Files=os.listdir('ch5')
numPages = len(ch5Files)

for i in range(0,numPages):
    path='ch5//'+ch5Files[i]
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