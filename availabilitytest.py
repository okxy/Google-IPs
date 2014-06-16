# Seek Google

import re
from urllib import request

url = r'https://github.com/okxy/Google-IPs'

def getdicturl(url):
    s = request.urlopen(url)
    html = s.read().decode('utf-8')
    country = re.findall('"anchor" href="#\w+?" aria', html)
    if not country[0]:
        """ s = re.findall('s','') #[]
        print('y' if s else 'n') #n
        ss= re.findall('\w?','') #['']
        print('y' if ss else 'n') #y
        """
        print('no country retrieved. check the url or re')
        return 0
    cts = [i[16:][:-6].title() for i in country]
    d = {i:[] for i in cts}
    y = html.find(cts[0])
    for i in range(1,len(cts)):
        z = html.find(cts[i], y)
        d[cts[i-1]].extend(re.findall('http\://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',html[y:z]))
        y = z
        print(cts[i-1], 'got')
    d[cts[-1]].extend(re.findall('http\://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',html[y:]))
    print(d['Bulgaria'])
    print(d['Japan'])
    return d


def dict2file(dct, f):
    with open(f, 'w', encoding='utf-8') as df:
        for i in sorted(dct):
            df.write(i)
            df.write('\n')
            for j in range(len(dct[i])):
                df.write(dct[i][j])
                if (j+1)%6 == 0 or j == len(dct[i])-1:  # save the '\n' at the end
                    df.write('\n')
                else:
                    df.write('\t')                
            df.write('\n')


'''http://stackoverflow.com/questions/8763451/how-to-handle-urllibs-timeout-in-python-3
The exception is timeout from socket, so

from socket import timeout
try:
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
except (HTTPError, URLError) as error:
    logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
except timeout:
    logging.error('socket timed out - URL %s', url)
else:
    logging.info('Access successful.')
'''

def testeddicturl(dicturl):
    dicturls = {}
    for i in dicturl:
        dicturls[i]=[] # i dicturl[i]
        for j in dicturl[i]: # don't del to change the list while iterating
            try:  # try positioning
                request.urlopen(j, timeout=1.6)
                dicturls[i].append(j)
            except:
                print(j, 'timeout, maybe')
                continue
        print(i,'tested')
    return dicturls

oldf = r'c:\Python\Google IP old.txt'
newf = r'c:\Python\Google IP new.txt'

dcturl = getdicturl(url)
dict2file(dcturl, oldf)
dict2file(testeddicturl(dcturl), newf)

def markdown():
    with open('Google IP new.txt', 'r', encoding='utf-8') as fr, open('Google IP new MD.txt', 'w', encoding='utf-8') as fw:
        s = fr.readlines()
        for i in s:
            if not i.startswith('htt'):
                fw.write(i)
                fw.write('--')
            else:
                line = i.split('\t')  # hope '\t' will save '\n'
                mdline = ['['+j[7:]+']'+'('+j+')' if not j.endswith('\n') else '['+j[7:-1]+']'+'('+j[:-1]+')\n' for j in line]  # if else position
                fw.write((' '*4).join(mdline))
            fw.write('\n')

markdown()
