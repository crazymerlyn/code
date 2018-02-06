from socket import *

try:
    skt = socket(AF_INET, SOCK_STREAM)
    skt.connect(("172.16.100.1", 22))
    skt.send('GET / HTTP/1.0\r\n\r\n')
    results = skt.recv(1000)
    print repr(str(results))
    skt.close()
except Exception, e:
    print "asfd"
    print(str(e))
