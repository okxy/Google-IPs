import time
from urllib import request
from collections import deque

def times(url, t = 3):
	t1 = time.time()
	for i in range(t):
		request.urlopen(url)
	t2 = time.time()
	print('time used: {0:.6f}'.format((t2-t1)/3))
	reutrn (t2-t1)/3

def fast(urllist):
    times = {}
    for i in urllist:
        times[i] = times(i)
    lstime = 0
    smtime = 0
    lst = []
    t = deque(times.keys(), 3)
    for i in urllist:
        if times[i] < times[t[2]]:
            t.append(i)
    return t

#fast()
