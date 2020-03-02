#__author:jack
#date 2020-02-09 13:55

from gevent import monkey; monkey.patch_all()
import gevent
from  urllib.request import urlopen
 
def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print(data)
    print('%d bytes received from %s.' % (len(data), url))
 
gevent.joinall([
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://github.com/'),
])