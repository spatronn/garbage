#git clone https://github.com/rthalley/dnspython
#python setup.py install

import dnspython as dns
import dns.resolver

filepath = 'a.txt'
with open(filepath, 'r') as fp:
    line = fp.readline().strip()
    while line:
        print(line)
        result = dns.resolver.query(line,'A')
        for ipval in result:
          print(ipval.to_text())
          ipaddr= ipval.to_text()
          x = open("exported.txt", "a")
          x.write(line+";"+ipaddr+'\n')
          x.close()
        line = fp.readline().strip()
