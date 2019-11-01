## DES算法实现
### 工具模块（util.py）
```
//16进制与二进制的装换
思路：
利用hex() int() bin()等函数
16进制 --> 10进制 --> 2进制
2进制 -->  10进制--> 16进制
```

### 子密钥生成模块(zimiyao.py)

```
//循环左移函数利用列表i的切片方法实现
def Listmove(l, step):    #将列表中的元素循环左移
    return l[step:] + l[:step]

//生成子密钥函数，首先将密钥列表用切片分为左右两组，循环左移后连接，最后置换选择出48bit密钥
//初始化好置换表，实现置换的方法并不困难

key_table2=[ 14, 17, 11, 24,  1,  5,
              3, 28, 15,  6, 21, 10,
             23, 19, 12,  4, 26,  8,
             16,  7, 27, 20, 13,  2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32 ]
             
 for i in range(len(key_table2)):           #key0是循环左移后连接得到的密钥列表
     key1[i] = key0[key_table2[i]-1]

```
#### 测试用例
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026154052105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)
### IP置换算法(ipreplace.py)


```
//初始化IP置换表，与逆IP置换表
与前面个的置换算法类似，判断op参数进行正逆置换

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
```

#### 测试用例
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026154202203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)

### f加密函数模块(ffun.py)
f加密函数，首先对32bit输入进行扩展运算位48bit数据，于密钥进行异或运算，核心加密部分为S盒置换，最终进行置换运算P输出结果

```
//调用工具模块整数转比特函数
//0~15整数转4位比特，留心不满4位前面补0，这里利用了zfill()函数
def int2bit(n):
    return list(bin(n)[2:].zfill(4))
```

#### 测试用例
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026163345571.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)

### DES加解密模块
根据流程依次调用前面写好的模块功能，就能实现加解密
#### 测试用例
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191026172144331.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODA5ODk2,size_16,color_FFFFFF,t_70)
