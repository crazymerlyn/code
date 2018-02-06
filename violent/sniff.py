from scapy.all import *
import sys
interface = 'mon0'

hidden = []
unhidden = []

def sniff1(pkt):
    if pkt.haslayer(Dot11ProbeResp):
        addr2 = p.getlayer(Dot11).add2
        if (addr2 in hidden) & (addr2 not in unhidden):
            name = pkt.getlayer(Dot11ProbeResp).info
            print name, addr2
            unhidden.append(addr2)
    if pkt.haslayer(Dot11Beacon):
        if pkt.getlayer(Dot11Beacon).info == '':
            addr2 = pkt.getlayer(Dot11).addr2
            if addr2 not in hidden:
                print addr2
                hidden.append(addr2)
        else:
            print(pkt.getlayer(Dot11Beacon).info)
sniff(iface=interface, prn=sniff1)
