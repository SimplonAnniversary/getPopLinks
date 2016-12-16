from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import concurrent.futures
import urllib.request

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
    
http = urllib3.PoolManager()
r = http.request('GET', url, preload_content=False)


with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for a in getLinks():
        print(a)

    
type(getLinks())
# print("type getLinks: "+type(getLinks()))
print(dir(getLinks()))

# print("type a: "+type(getLinks()))
# print("dir a: " +(a))



