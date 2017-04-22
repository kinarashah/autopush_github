import cookielib
import requests 
import json
import sys 

PATH = 

def retrieve(url, headers=None, data=None, method='GET'):
    try:
        if method == 'GET':
            r = session.get(url, headers=headers)
        elif method == 'POST':
            r = session.post(url, headers=headers, data=data)
        return r 
    except:
        print("Network Error "+url)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection': 'keep-alive',
    'Host': 'leetcode.com',
    'Referer': 'https://leetcode.com/accounts/login/'
}

