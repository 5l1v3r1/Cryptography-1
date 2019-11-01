'''
@Author: huha
@Date: 2019-10-26 16:57:11
@LastEditTime: 2019-10-26 17:04:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \DES实验\des\binhex.py
'''
#十六进制转二进制比特串
def Hex2bin(text):
    hexstr = '0x'+text
    decstr = int(hexstr,16)
    binstr = int2bit(decstr,64)
    # print(binstr)
    # print(len(binstr))
    return binstr
#二进制比特串转十六进制
def bin2Hex(text):
    binstr = '0b' + "".join(text)
    hexstr = hex(int(binstr,2))[2:]
    return hexstr

#0~15整数转比特   
def int2bit(n,limit): 
    return list(bin(n)[2:].zfill(limit))