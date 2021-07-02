# /hunter-comic/
import json
import os
from bs4 import BeautifulSoup
import lxml


## Main functions ##


ch6Files=os.listdir('ch6')
numPages = len(ch6Files)

for i in range(0,numPages):
    path='ch6//'+ch6Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    mylinks = soup.findAll('a')
    
    for i in range(0,len(mylinks)):
        mylinks[i]["href"] = "/hunter-comic"+mylinks[i]["href"]
 
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))