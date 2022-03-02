#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[24]:


# Input glasses code from site
Barcode=input("please enter sunglsses barcode: ")
cv_img = plt.imread('D:/WORK/Cheshmyar/color filtering task/Dataset filter colors/Highlight/'+ Barcode +'.jpg')    
cv_img = cv_img.copy()
cv_img = cv_img.astype("int")


# In[25]:


# input picture from customer and adding more contrast
customer_img = plt.imread('C:/Users/asus/Desktop/targetgirl1.jpg')
customer_img = customer_img.copy()
customer_img = customer_img.astype("int")
contrast=40
img_con = customer_img * (contrast/127 + 1 ) - contrast
img_con = np.clip(img_con, 0, 255)
img_con = img_con.astype("uint8")


# In[26]:


def total_def():
    img_blend = cv_img*0.4 + img_con* 0.6
    img_blend = np.clip(img_blend, 0, 255)
    img_blend = img_blend.astype("uint8") 


# In[27]:


total_def()

