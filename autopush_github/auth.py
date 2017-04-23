import cookielib
import requests 
import json
from config import USERNAME, PASSWORD

PATH = 'cookies'
BASEURL = 'https://leetcode.com/'
AUTHURL = BASEURL + 'accounts/login/'
APIURL = BASEURL + 'api/problems/algorithms/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection': 'keep-alive',
    'Host': 'leetcode.com',
    'Referer': 'https://leetcode.com/accounts/login/'
}

session = requests.Session()
session.cookies = cookielib.LWPCookieJar(path)

try:
    session.cookies.load(ignore_discard=True)
except:
    pass

def retrieve(url, headers=None, data=None, method='GET'):
    try:
        if method == 'GET':
            r = session.get(url, headers=headers)
        elif method == 'POST':
            r = session.post(url, headers=headers, data=data)
        return r 
    except:
        print("Network Error "+url)

def login():
    r = retrieve(AUTHURL, headers=headers)
    if r.status_code!=200:
        print("Login Error")
        return False

    login_helper = {} 

    if 'csrftoken' in r.cookies:
        csrftoken = r.cookies['csrftoken']
        login_helper['csrfmiddlewaretoken'] = csrftoken

    login_helper['login'] = USERNAME
    login_helper['password'] = PASSWORD
    login_helper['remember'] = 'on'

    r = retrieve(AUTHURL, headers=headers, data=login_helper, method='POST')
    if r.status_code!=200:
        print("Login Error")
        return False

    session.cookies.save()
    print("Login Successful")
    return True 

def isloggedin():
    r = retrieve(APIURL)
    if r.status_code!=200:
        return False 
    data = json.loads(r.text.encode('utf-8'))
    return 'user_name' in data and data['user_name']
