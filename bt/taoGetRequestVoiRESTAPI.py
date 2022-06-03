# gui request http lay thong tin ve host
import requests, json
response = requests.get("http://httpbin.org/get",timeout=5)
print("HTTP Status Code: " + str(response.status_code))
print(response.headers)
if response.status_code == 200:
    results = response.json()
    for results in results.items():
        print(results)
    print("Headers response: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
    print("Header request : ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
        print("Server: " + response.headers['server'])
else:
    print("Error code %s" %response.status_code)
    
