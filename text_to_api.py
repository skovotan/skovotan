import requests

with open('text.txt') as f:
    for line in f:
        if 'cname:' in line:
            a, nameb, namec = line.split()
            #cname = name.split()
            #print('{}{}{}'.format(a, b, c))
        elif 'ip:' in line:
            host = line.split()[-1]
        elif 'ce_hostname:' in line:
            hostname = line.split()[-1]
            #print('{}'.format(hostname))
        elif 'ico:' in line:
            ico = line.split()[-1]
        elif 'srid:' in line:
            srid = line.split()[-1]
            output = '{}{}{}{}{}{}{}{}{}{}{}'.format('&name=', 'SRID:', srid, ' ', nameb, ' ', namec, '&tags=', ico, '&host=', host)
            print(output)
            y = 'https://test.com/api/duplicateobject.htm?id=88951' + output + '&targetid=86713&username=xxxx&passhash=xxxxxx'
            #print(y)            
            x = requests.post(y)
