# /hunter-comic/
import json
import os
from bs4 import BeautifulSoup
import lxml


## Main functions ##


ch1Files=os.listdir('ch1')
numPages = len(ch1Files)

for i in range(0,numPages):
    path='ch1//'+ch1Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    mylinks = soup.findAll('link')
    
    for i in range(0,len(mylinks)):
        mylinks[i]["href"] = "/hunter-comic"+mylinks[i]["href"]
 
    with open(path, "w") as ogfile:
       ogfile.write(str(soup))