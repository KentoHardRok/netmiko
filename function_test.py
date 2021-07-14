#!/usr/bin/python3
# -*- coding: utf-8 -*-



def ip_increment(host, count):
    ip_list=[]
    octets = host.split(".")
    int_octets = list(map(int, octets))
    for i in range(count):
        int_octets[3] += i
        ip_list.append['.'.join(list(map(str, int_octets)))]
    return(ip_list)
        
ip_increment("192.168.100.101", 8)



