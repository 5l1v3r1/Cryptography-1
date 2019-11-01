'''
@Author: huha
@Date: 2019-10-26 13:21:22
@LastEditTime: 2019-10-26 15:41:31
@LastEditors: Please set LastEditors
@Description: IP置换算法模块，包含正逆IP置换
@FilePath: \DES实验\des\ipreplace.py
'''
#IP置换表
IP_table=[58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17,  9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7 ]
#逆IP置换表
Inv_IP_table=[40,  8, 48, 16, 56, 24, 64, 32,
              39,  7, 47, 15, 55, 23, 63, 31,
              38,  6, 46, 14, 54, 22, 62, 30,
              37,  5, 45, 13, 53, 21, 61, 29,
              36,  4, 44, 12, 52, 20, 60, 28,
              35,  3, 43, 11, 51, 19, 59, 27,
              34,  2, 42, 10, 50, 18, 58, 26,
              33,  1, 41,  9, 49, 17, 57, 25 ]
              
#IP置换部分，op为0表示正置换，op为1表示逆置换
def IP(text, op):   
    tmp = [0 for i in range(64)]
    if op == 0:
        for i in range(64):
            tmp[i] = text[IP_table[i]-1]
        return tmp
    if op == 1:
        for i in range(64):
            tmp[i] = text[Inv_IP_table[i]-1]
        return tmp

if __name__ == "__main__":
    keystr = '1010100110101001101010011010100110101001101010011001101010011010'
    keylist = list(keystr)
    ipkeylist = IP(keylist,0)
    print("".join(ipkeylist))
    ipkeylist = IP(keylist,1)
    print("".join(ipkeylist))
    