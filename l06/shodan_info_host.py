#!/usr/bin/env python
# thu thap thong tin ve may chu
import requests
import os

SHODAN_API_KEY = "ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8"  #os.environ['ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8']
ip = '42.112.213.84'

def ShodanInfo(ip):
    try:
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minify=True").json()
    except Exception as exception:
        result = {"error":"Information not available"}
    return result

print(ShodanInfo(ip))

# https://api.shodan.io/shodan/host/{ip}?key=ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8
