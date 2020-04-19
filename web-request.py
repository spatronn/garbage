#  pip instal requests
import requests

filepath = 'a.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       web_site= (line.strip())
       req = requests.get("http://"+web_site)
       print(web_site,'status :',req.status_code)
       line = fp.readline()
