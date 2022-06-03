import urllib.request
from urllib.request import Request

from requests import request
url = "http://actvn.edu.vn"
USER_AGENT = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"
def chrome_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    print("Response headers")
    print("---------------------------")
    for header, value in response.getheaders():
        print(header + ":" + value)
    request = Request(url)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("-------------------------------")
    for header, value in request.header_items():
        print(header + ":" + value)
if __name__ == '__main__':
    chrome_user_agent()

