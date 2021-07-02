# time to replace images AGAIN!!
import json
import os
from bs4 import BeautifulSoup
import lxml

imageList=os.listdir('panels')
imageCounter = 0

ch1Files=os.listdir('ch1')
numPages = len(ch1Files)

for i in range(0,numPages):
    path='ch1//'+ch1Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))
    break
