# Google PI Availability Test

import re
from urllib import request

url = r'https://github.com/okxy/Google-IPs'
def getdicturl(url):
    s = request.urlopen(url)
    html = s.read().decode('utf-8')
    country = re.findall('"6">\w+?</th>', html)
    cts = [i[4:][:-5] for i in country]
    d = {i:[] for i in cts}
    y = html.find(cts[0])    
    for i in range(1,len(cts)):
        z = html.find(cts[i], y)
        d[cts[i-1]].extend(re.findall('http\://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',html[y:z]))
        y = z
    #    print(cts[i-1], 'got')
    d[cts[-1]].extend(re.findall('http\://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',html[y:]))
    #print(d['Bulgaria'])
    #print(d['Japan'])
    return d



def dict2file(dct, f):
    with open(f, 'w', encoding='utf-8') as df:
        for i in sorted(dct):
            df.write(i)
            df.write('\n')
            for j in range(len(dct[i])):
                df.write(dct[i][j])
                df.write('\t')
                if (j+1)%5 == 0:
                    df.write('\n')
            df.write('\n')


def testeddicturl(dicturl):
    dicturls = {}
    dicturlomg = {}
    for i in dicturl:
        dicturls[i] = [] # i dicturl[i]
        dicturlomg[i] = []
        for j in dicturl[i]: # don't del to change the list while iterating
            try:
                request.urlopen(j, timeout=3)
                dicturls[i].append(j)
            except:
                print(j)
                dicturlomg.append(j)
        #print(i,'tested')
    return dicturls, dicturlomg

oldf = r'c:\Python\Google IP old.txt'
newf = r'c:\Python\Google IP new.txt'
badf = r'c:\Python\Google IP bad.txt'

dcturl = getdicturl(url)
td = testeddicturl(dcturl)
dict2file(dcturl, oldf)
dict2file(td[0], newf)
dict2file(td[1], badf)

















        
