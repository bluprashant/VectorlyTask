# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:14:03 2020

@author: katsh
"""

import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    bw_input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(bw_input_image)  
    cl1 = cv2.bitwise_not(cl1)
    ret3,th3 = cv2.threshold(cl1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((7,7),np.uint8)
    erod = cv2.erode(th3,kernel,iterations = 1)
    output = cv2.bitwise_not(erod)

     
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('C:/Users/katsh/OneDrive/Desktop/simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################