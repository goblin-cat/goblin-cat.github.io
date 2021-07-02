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
        
##


ch2Files=os.listdir('ch2')
numPages = len(ch2Files)

for i in range(0,numPages):
    path='ch2//'+ch2Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))

# done w ch2


ch3Files=os.listdir('ch3')
numPages = len(ch3Files)

for i in range(0,numPages):
    path='ch3//'+ch3Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))



ch4Files=os.listdir('ch4')
numPages = len(ch4Files)

for i in range(0,numPages):
    path='ch4//'+ch4Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))


ch5Files=os.listdir('ch5')
numPages = len(ch5Files)

for i in range(0,numPages):
    path='ch5//'+ch5Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))


ch6Files=os.listdir('ch6')
numPages = len(ch6Files)

for i in range(0,numPages):
    path='ch6//'+ch6Files[i]
    file = open(path,'r')
    page = file.read()
    soup = BeautifulSoup(page, 'lxml')
    
    myImages = soup.findAll('img',{"class": "panel"})
    
    for i in range(0,len(myImages)):
        imageCounter += 1
        myImages[i]["src"]='/hunter-comic/panels/'+str(imageCounter) + '.png'
    
    with open(path, "w") as ogfile:
        ogfile.write(str(soup))


            


