#!/usr/bin/env python
# -*- coding: utf8 -*-
from datetime import *
import os
import sys
path='./include'
sys.path.insert(0,path)
import sendsms_api as sms
import functions as func

send_sms_to_list = func.get_option('send_sms_to_list')
sms_to_list=send_sms_to_list.split(';')
sms_to_list_comma = ",".join(sms_to_list)
sms_msg = 'Hello Lepus!' 

sms.send_sms(sms_to_list, sms_msg,1,1,1,1,1,1,1,1)
