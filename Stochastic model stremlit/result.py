# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:54:30 2021

@author: HP
"""
# import library

import credentials
from pymongo import MongoClient


# defining the password
key = credentials.login['key_isaham']


# Obtaining variables from environment variables
user = credentials.login['username_db']
pwd = credentials.login['password_db']
ip = credentials.login['ip_db']
port = credentials.login['port_db']


# Access to cluster
master_client = MongoClient("mongodb://{}:{}@{}:{}".format(user,pwd,ip,port))


# Accessing mongodb database
db = master_client['Trading_Prediction']


# Accessing collection
col = db['Stochastic_strategy']


# saving the prediction into dataframe
# pulling the latest 1
res_dct = col.find().sort("_id", -1)[0]
print(res_dct)