#-*- coding:utf-8 -*-

import urllib, time

config = {
    'login_email':'ACCOUNT',
    'login_password':'PASSWORD',
    'format':'json',
    'domain_id':'XXXXXXXX',
    'record_id':'XXXXXXXX',
    'record_line':'默认',
    'sub_domain':'SUBDOMAINNAME',
    'value':''
}

api = {
    'domain':'https://dnsapi.cn/Domain.List',
    'record':'https://dnsapi.cn/Record.List',
    'info':'https://dnsapi.cn/Record.Info',
    'ddns':'https://dnsapi.cn/Record.Ddns'
}

def ddns(ip):
    config['value'] = ip
    _params = urllib.urlencode(config)
    _f = urllib.urlopen(api['ddns'], _params)
    _out = _f.read()
    _f.close()
    print _out
    return _out

def ipaddr():
    _f = urllib.urlopen('http://ifconfig.me')
    _ip = _f.read()
    return _ip

current_ip = None

if __name__ == '__main__':
    while True:
        try:
            _ip = ipaddr()
            print _ip
            if current_ip != _ip:
                if ddns(_ip): current_ip = _ip
        except Exception, e: print e
        time.sleep(30)
