import urllib.request
from bs4 import BeautifulSoup
import re
import os
import time
import progressbar

# Fucntion to get links from html code.

def getLinks():
    html = open("html.txt")                                                            # List of links
    bsObj = BeautifulSoup(html.read(), "lxml")                                         # Beautify HTML with BS4
    imageList = bsObj.findAll("div", {"class":"item-image"})                           # Get only all with class 'item-image'
    x = 0                                                                              # Iterator for filenames and stuff.
    aList = []                                                                         # Make a list   
    for image in imageList:                                                            # For every images in the list
        if "ab" in image["style"]:                                                     # Only if has "ab" in filename (ab1023...jpg)
            x = x  + 1                                                                 # Increment file iterator
            a = image["style"]                                                         # Put style attribute in string
            a_strip = a[22:99]                                                         # Get only this part
            aList.append(a_strip)                                                      # Add to list
    return aList
        

n = 0                                                                                  # Iterator
strLength = len(getLinks())                                                            # Store length of list of links
path = "images/"                                                                       # Directory for images
bar = progressbar.ProgressBar(max_value=strLength,redirect_stdout=True)                # Create an instace of ProgressBar


print(str(strLength)+" Objects")                                                       # Print number of items in list
print("Checking or creating 'images/'..")                                              
os.makedirs(path, exist_ok=True)                                                       # Check for 'images/' 



for a in getLinks():                                                                   # For every image in return of getLinks()
    url = a 
    urllib.request.urlretrieve(url, path + str(n) + '.jpg')                            # Get image
    n = n + 1                                                                          # Iterate n (+1)
    print("Downloading " + path  + str(n)+".jpg")                                      # Output to user
    bar.update(n)                                                                      # Update progress bar..

    
