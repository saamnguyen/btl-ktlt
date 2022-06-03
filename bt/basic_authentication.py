#!/usr/bin/env python3
# xac thuc co ban bang http su dung dinh dang user:password
from email.policy import HTTP
from urllib import response
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
username=input("Enter username:")
password =getpass()
response = requests.get('https://github.com/login',auth=HTTPBasicAuth(username,password)) #thay đổi url
print('Response.status_code:'+str(response.status_code))

if response.status_code == 200:
    print('Login succcessful : '+ response.text)