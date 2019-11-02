# coding:utf-8
import random
import util

def get_key():
    p = random.randint(0,65535)
    q = random.randint(0,65535)
    e = random.randint(0,65535)
    while not util.is_Prime(p):
        p = p+1
    while not util.is_Prime(q):
        q = q+1
    n = q*p
    o = (p-1)*(q-1)
    # e的需要与o互质
    while util.ext_rec(o,e)[0] != 1:
        e = e+1
    d = util.ext_res(o,e)
    return e,n,d,o

m1 = 688
e,n,d,o = get_key()
print('e: '+str(e))
print('n: '+str(n))
print('o: '+str(o))
print('d: '+str(d))
c = util.quick_pow(m1,e,n)
m2 = util.quick_pow(c,d,n)
print(c)
print(m2)
if m2 == m1:
    print('明文: ',m1)
    print('密文: ',c)

