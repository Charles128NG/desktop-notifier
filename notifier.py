#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:31:08 2020

@author: charles
"""
import time
import notify2
from top_news import top_story_sender


def notification_sender():
    
    
    news_recevied =  top_story_sender()
    
    notify2.init('notifier')#itializer for d bus
    
    n = notify2.Notification(None) #notification object
    
    n.set_urgency(notify2.URGENCY_NORMAL)
    
    n.set_timeout(10000)
    
    for news in news_recevied:
        n.update(news['title'],news['description'])
        
        n.show()
        
        time.sleep(15000)
        
        
        

notification_sender()

    
    
    

    
