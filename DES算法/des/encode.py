'''
@Author: huha
@Date: 2019-10-26 12:50:20
@LastEditTime: 2019-10-26 17:03:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \DES实验\des\encode.py
'''
import zimiyao as cs
import ffun as f
import ipreplace as ip
import util
#按照DES算法的流程图进行运算
def Encryption(text, key):
    keylist = cs.Subkey(keybit)
    text1 = ip.IP(text, 0)  #IP置换
    L = [text1[i] for i in range(32)]
    R = [text1[i] for i in range(32,64)]
    for i in range(16):
        tmp = R
        tmp = f.ffun(tmp, keylist[i])
        tmp = f.Xor(tmp, L)
        L = R
        R = tmp
    L,R = R,L
    # print(L)
    # print(R)
    # return
    ctext = L
    ctext.extend(R)
    ctext = ip.IP(ctext, 1)
    return util.bin2Hex(ctext)

if __name__ == '__main__':
    plaintext = input('请输入16位用十六进制表示的明文：')
    key = input('请输入16位用十六进制表示的密钥：')
    ptext = util.Hex2bin(plaintext)
    keybit = util.Hex2bin(key)
    # Encryption(ptext, keybit)
    print('输出的密文为：' + Encryption(ptext, keybit))