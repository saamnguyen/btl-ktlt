# import socket
# from unittest import result
# ip = '42.113.206.26'
# portlist = [21,22,23,80,443]
# for port in portlist:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((ip,port))
#     print(port,":",result)
#     sock.close()

#----------------------------------------------------------
import http.client
connection = http.client.HTTPConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)
if response.status == 200:
    data = response.read()
    print(data)