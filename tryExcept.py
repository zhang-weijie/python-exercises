from urllib.request import Request,urlopen
from urllib.error import URLError

def main():
    url=input('请输入URL:')
    req=Request(url)
    try:
        response=urlopen(req)
    except URLError as e:
        if hasattr(e,'reason'):
            print('We failed to reach the server.')
            print('Reason:',e.reason)
        elif hasattr(e,'code'):
            print('The server couldn\'t fullfil the request.')
            print('Error code',e.code)

if __name__=='__main__':
    main()
