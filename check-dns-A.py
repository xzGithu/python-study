#!/usr/bin/ python


import dns.resolver

domain=raw_input('your domain name:')

A=dns.resolver.query(domain,'A')

for i in A.response.answer:
    for j in i.items:
        print j.address
