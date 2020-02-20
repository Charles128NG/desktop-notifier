#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:50:33 2020

@author: charles
"""

import requests
import xml.etree.ElementTree as ET


#function to get news conent

def news_getter():
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"    
    response = requests.get(url)
    return response.text
#function to parse the xml content of wep bage
def parserfn(rss):
    root = ET.fromstring(rss)
    
    news = []# to store news
    
    for item in root.findall('./channel/item'):
        news_item = {}  #create a dictionary for every new news as pasred from the website"""
        
        for child in item :# travese thru the news to get meaningful info
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news_item['media'] = child.attrib['url']
            else:
                news_item[child.tag] = child.text
                
        news.append(news_item)
        
        
    return news
 #fn to reurn news for sending notification
def top_story_sender():
     rss=news_getter()
     
     news = parserfn(rss)
      
     return news
     

