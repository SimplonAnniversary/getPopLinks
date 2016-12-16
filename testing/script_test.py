import urllib.request
from bs4 import BeautifulSoup
import re
import time
import progressbar

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
    aList = []
    for image in imageList:
        if "ab" in image["style"]:     # has "ab" in filename (ab1023...jpg)
            x = x  + 1
            a = image["style"]        # put style in variable
            a_strip = a[22:99]
            aList.append(a_strip)
            # print(str(x)+": "+a_strip)
    return aList
        
            #            if a is not None:
#                print(a[22:99])           # get the right position and amount of characters - selection
    


n = 0
strLength = len(getLinks())
bar = progressbar.ProgressBar(max_value=strLength,redirect_stdout=True)


print(str(strLength)+" Objects")

for a in getLinks():
    url = a
    # image = url.rsplit('/', 1)[1]
    urllib.request.urlretrieve(url, str(n)+'.jpg')
    n = n + 1
    print("Downloading "+str(n)+".jpg")
    bar.update(n)

    
# print("type getLinks: "+type(getLinks()))
# print(dir(getLinks()))

# print("type a: "+type(getLinks()))
# print("dir a: " +(a))



