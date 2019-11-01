#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc:
author: huha
'''
class xor:
    def __init__(self,key):
        self.key = key
    def en(self,a):
        enstr = bytearray()
        for x in range(len(a)):
            enstr.append(a[x]^self.key[x%len(self.key)])
        return enstr

    def de(self,enstr):
        a = bytearray()
        for x in range(len(enstr)):
            a.append(enstr[x] ^ self.key[x % len(self.key)])
        return a

    def enfile(self,file):
        a = file.read()
        with open(file.filename+'_en','wb') as f:
            f.write(self.en(a))

    def defile(self,file):
        enstr = file.read()
        with open(file.filename+'_de','wb') as f:
            f.write(self.en(enstr))


if __name__ == '__main__':
    a = bytes('sdfadf','utf8')
    key = bytes('123_哈', 'utf8')
    xor = xor(key)
    enstr = xor.en(a)
    print(xor.de(enstr).decode())