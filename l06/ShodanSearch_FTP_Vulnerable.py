#!/usr/bin/env python
# su dung shodan tim kiem cac server co dich vu FTP - cong 21 de bi tan cong
import shodan
import re
import os

servers =[]
shodanKeyString = "ptNfQMuGKFphM8Y7D8unwhhTZJCSlLJ8"
shodanApi = shodan.Shodan(shodanKeyString)

results = shodanApi.search("port: 21 Anonymous user logged in")
print("hosts number: " + str(len( results['matches'])))
for result in results['matches']:
	if result['ip_str'] is not None:
		servers.append(result['ip_str'])
		
for server in servers:
    print(server)