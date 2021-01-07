# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:33:41 2021

@author: saime
"""

import glassdoor_scraper as gs
import pandas as pd

path="C:/Users/saime/Documents/Kaggle/survey_Project-2020/chromedriver"
df=gs.get_jobs('data scientist',15, False,path,15)

df