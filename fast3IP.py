import time
from urllib import request
from collections import deque

def urltime(urls, t = 3):

    """ return dict of url: time """

    urltimes = {}

    for url in urls: # mind that don't mistake the token in nested loop!

        try:
            ts = 0
            for i in range(t):
                t1 = time.time()
                request.urlopen(url, timeout = 1.5)
                t2 = time.time()
                ts += (t2-t1)
            print('{0}: {1:.6f}'.format(url,ts/t))
            urltimes.update({url:ts/t})

        except:
            print('{0}: time out'.format(url))

    return urltimes

def fast(urltimes, n=3):

    """return the fastest n urls"""

    t = deque(urltimes.keys(), n)


    for i in urltimes:
        print('urltimes[i]', urltimes[i])        
        if urltimes[i] < urltimes[t[-1]]: 
            t.append(i)

    fastn = {i:urltimes[i] for i in t}  # TypeError: unhashable type: 'collections.deque'

    return fastn


def readip():
    with open('Google IP new.txt', 'r', encoding='utf-8') as fr, open('fast3.txt', 'w', encoding='utf-8') as fw:

        # read ip into list
        ips = []
        s = fr.readlines()
        for i in s:
            if i.startswith('http'):
                line = i.split()
                ips.extend(line)
        for i in ips:
            print(i)
        # get ip:time
        fastipdic = fast(urltime(ips))      

        # write ip:time into file
        for i in fastipdic:
            fw.write(i+':\t'+str(fastipdic[i]))  # TypeError: 'dict' object is not callable  TypeError: write() takes exactly 1 argument (2 given)
            fw.write('\n')    

readip()
