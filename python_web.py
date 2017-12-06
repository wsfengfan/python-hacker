import urllib
import urllib2
import threading
import sys

try:
    url = sys.argv[1]
except:
    print "[!] Usage: [target_url] "
    sys.exit(0)

try:
    fp = open("all.txt","r")
    fp_file = fp.readlines()
    fp.close()
except:
    print "[!] File to error."
    sys.exit(0)

try:
    for url_word in fp_file:
        _url_ = "%s/%s"%(url, url_word)
        r = urllib2.Request(_url_)
        url_data = urllib2.urlopen(r)
        if len(url_data.read()):
            print "[%d] ==> %s"%(url_data.code, _url_)
except KeyboardInterrupt:
    print "[!] Stop"
    sys.exit(0)

