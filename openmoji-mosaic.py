import pyautogui
import os
from PIL import Image
import numpy as np
import time
import random
import string

imgList = []
arr = []
selArr = []

xStep = 500
yStep = 100
nameCount = 0


# wait to get ready
time.sleep(2)

#minimze code 

# get color layout of target img
imgOG = Image.open('src/goal.png')
imgComp = imgOG.resize((25, 24))
#imgComp.show()

imageArray = np.array(imgComp)
#print(imageArray)

for row in imageArray:

    #count y step up, reset x step
    yStep = (yStep + 25)
    xStep = 500

    for pix in row: 

        # def randString(length=5):
        #     your_letters='abcdefghijklmnopqrstuvwxyz'
        #     return ''.join((random.choice(your_letters) for i in range(length)))

        # count x step up; count name-count up
        xStep = (xStep + 25)
        nameCount = (nameCount+1)
        #print(nameCount)
         
        posVal = np.amax(pix)
        print(posVal) # get avg value

        # select lib window
        pyautogui.moveTo(x=210, y=325)
        pyautogui.mouseDown(); pyautogui.mouseUp() 
        time.sleep(0.5)
        
        # iterate key-down through np.amax list
        pyautogui.typewrite(str(posVal), interval=0) # insert var instead of numb 
        time.sleep(0.25)

        # move mouse down to selection area
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('src/goal.png'))
        time.sleep(0.25)
        pyautogui.mouseDown(); pyautogui.mouseUp() 
        time.sleep(0.25)

        # drag and drop to new folder 
        pyautogui.keyDown('alt') 
        pyautogui.dragTo(xStep, yStep, 0.5, button='left') # insert place to drag img here 

        # rename 
        # pyautogui.moveTo(x=xStep, y=yStep)
        # pyautogui.mouseDown(); pyautogui.mouseUp() 
        # pyautogui.keyDown('enter') 
        # time.sleep(1)
        # pyautogui.typewrite(randString(), interval=0)
        # pyautogui.keyDown('enter')
        # time.sleep(1)

        # select lib window
        pyautogui.moveTo(x=55, y=325)
        pyautogui.mouseDown(); pyautogui.mouseUp() 
        time.sleep(0.25)

        # iterate key-down through np.amax list
        # pyautogui.typewrite('000', interval=0)
        # pyautogui.scroll(50) 
        # time.sleep(0)



### ### ### ### ### ### ### ### ###### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
### ### ### ### ### ### ### ### ###### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
### ### ### ### ### ### ### ### ###### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 




##sort images by their avg color val 
# for filename in os.listdir():
#     if filename.endswith(".png"):
#       img1 = Image.open(filename).convert('LA')
#       img2 = img1.resize((1,1))
#       myColor, myAlpha = img2.getpixel((0,0))
#       arr  = [myColor, filename]
#       newName = myColor
#       print(filename, newName)
#       imgList.append(arr)
#       imgList.sort()
#       #print (imgList)  
#       os.rename(filename, str(newName) + '.png')