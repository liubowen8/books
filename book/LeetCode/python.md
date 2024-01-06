python
--------------------------

python没有字符char这个数据类型，一个字母也是字符串
x='a' 这里的x也是字符串，只不过字符串的长度为1
x=“asd” 这也的字符串长度为3。这一点和c++还是不同的。字符串有几个字母长度就是几，后面没有累加’\n‘字符。

python字符之间比较大小，计算差距

ord(字符) 返回这个字符对于的ASCII码
chr(数字)，输入一个0-255的数字，返回这个数字对应的字符

---------------

1：选择最少的人数，让他们覆盖整体：

![图片12](E:\images\图片12.png)
------------

--------------

2：回溯算法

```python
x= [1,2,3,4]
vis=[0]*len(x)
temp=[]

def digui(start,end,x):
  global temp
  if len(temp) == 4 : 
    print(temp)
    return 
  else :
    for i in range(start, end+1):
      if vis[i]==0 :
        # 这两步是把珠子push到temp中
        temp.append(x[i])
        vis[i]=1
        # 这两步是把珠子push到temp中
        digui(start, end,x) # 递归步骤
        # 这两步是把珠子从temp中pop出来
        temp.pop()
        vis[i]=0     
		# 这两步是把珠子从temp中pop出来
digui(0,3,x)
```

--------

函数的值传递和引用传递：
![image-20230820000240444](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20230820000240444.png)
说是如果使用的是可变的数据类型： 列表、集合、字典(引用传递)
字符串、数组和元组使用值传递。
![图片17](E:\images\图片17.png)
如果是列表、结合、字典，那么可以不用写形参直接使用，如果是字符串、数字、元组那么在函数使用时，必须要有形参存在。
![image-20230820004214831](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20230820004214831.png)
函数中的函数，对函数中的local变量进行修改，需要引用传递，但是只有在数据类型为列表、集合或者字典的时候才会进行引用传递。

位逻辑运算：&，|，！，^ （与，或，非，）

士大夫