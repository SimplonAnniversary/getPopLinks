from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#html = urlopen("https://www.poparchiefgroningen.nl/podia/simplon/view")
def getLinks():
    html = open("html.txt")
    bsObj = BeautifulSoup(html.read(), "lxml")
    
    # print("Print all Headers")
    # print (bsObj)
    print("Print all item-image objects")
    imageList = bsObj.findAll("div", {"class":"item-image"})
    # print(dir(imageList))
    # imageList = bsObj.findAll("div", style=re.compile("*\/artwork\/*"))
    # pattern = re.compile("*\/artwork\/*\.jpg$")
    # pattern.search(bsObj)
    x = 0
    for image in imageList:
        if "ab" in image["style"]:     # has "ab" in filename (ab1023...jpg)
            x = x  + 1
            a = image["style"]        # put style in variable
            a_strip = a[22:99]
            print(str(x)+": "+a_strip)
            
        
            #            if a is not None:
#                print(a[22:99])           # get the right position and amount of characters - selection
    

getLinks()
