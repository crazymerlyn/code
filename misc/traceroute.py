from scapy.all import *

hostname = 'www.duckduckgo.com'
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=12345)
    reply = sr1(pkt, verbose=0, timeout=1)
    if reply is None:
        print "Timeout"
        continue
    elif reply.type == 3:
        print "Done"
        break
    else:
        print "%d hops away" % i, reply.src
