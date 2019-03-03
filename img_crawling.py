import time
import requests
import urllib.request
import cv2
import numpy as np
import os
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
browser = webdriver.Chrome('D:\Python\driver\chromedriver_win32\chromedriver.exe', chrome_options=options)

def neg_img(word):
  url = 'https://www.google.co.kr/search?q=' + word + '&tbm=isch'
  browser.get(url)
  elem = browser.find_element_by_tag_name("body")  

  no = 5
  while no:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    no -= 1
    
  cnt = 1
  img_list = list()
  img = browser.find_elements_by_class_name("rg_ic")

  for i in img:
    img_list.append(i.get_attribute("src"))

  for i in img_list:
    try:
      print(i)
      urllib.request.urlretrieve(i, "act/" + str(cnt) + ".jpg")
      # img = cv2.imread("act/" + str(cnt) + ".jpg", cv2.IMREAD_GRAYSCALE)
      # resized_image = cv2.resize(img, (100, 100))
      # cv2.imwrite("act/"+str(cnt)+".jpg", img)
      cnt += 1
    except Exception as e:
      print(str(e))

def pos_img():
  url = 'https://www.google.co.kr/search?q=남자+배우&tbm=isch'
  browser.get(url)
  elem = browser.find_element_by_tag_name("body")  
  
  no = 4
  while no:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    no -= 1

  cnt = 1
  img_list = list()
  img = browser.find_elements_by_class_name("rg_ic")

  for i in img:
    img_list.append(i.get_attribute("src"))

  for i in img_list:
    try:
      print(i)
      urllib.request.urlretrieve(i, "pos/" + str(cnt) + ".jpg")
      img = cv2.imread("pos/" + str(cnt) + ".jpg", cv2.IMREAD_GRAYSCALE)
      # resized_image = cv2.resize(img, (100, 100))
      cv2.imwrite("pos/"+str(cnt)+".jpg", img)
      cnt += 1
    except Exception as e:
      print(str(e))

def create_pos_n_neg():
  for file_type in ['neg', 'pos']:
    for img in os.listdir(file_type):
      if file_type == 'pos':
        line = file_type + '/' + img + '\n'
        with open('positives.txt', 'a') as f:
          f.write(line)
      elif file_type == 'neg':
        line = file_type+'/'+img+'\n'
        with open('negatives.txt', 'a') as f:
          f.write(line)
