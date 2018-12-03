import urllib.request
import time


def http_request(url):
    start = time.time()
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        response.getheaders()
        end = time.time()
        b = response.getheader('Content-Length')

    t = float(end - start)
    bts = int(b)
    speed = int(bts/t)

    return [t, bts, speed]
