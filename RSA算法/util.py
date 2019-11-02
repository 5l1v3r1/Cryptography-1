#  扩展欧几里得递归算法
# m * x + n * y = 1

def ext_res(n,e):
    d = ext_rec(n,e)[2]
    if d<0:
        d = d+n
    return d

def ext_rec(m, n):
    if(n == 0):
        return m,1,0
    r,x,y = ext_rec(n, m%n)  
    t = y
    y = x-int(m/n) * y
    return r, t, y

def is_Prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            return False
    return True

def quick_pow(a, b, c):
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a % c) * (a % c)
    return ans

if __name__ == "__main__":
    # 扩展欧几里得算法
    # n = 3220
    # e = 17
    # print(ext_res(n,e))
    # # # 快速求模运算
    print(quick_pow(688,79,3337))
    # print(quick_pow_mod(688,79,3337))
    # 判断时候素数
    # print(is_Prime(79))
        
        