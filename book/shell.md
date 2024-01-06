Shell && Linux
----------

alias 用于给指令起别名： alias [别名]=[指令名称]

awk 文本分析工具
echo $SSH_CLIENT | awk '{print $1}' 
<img src="E:\images\图片14.png" alt="图片14" style="zoom: 67%;" />
管道的作用。

----------------

![图片15](E:\images\图片15.png)

------------------

dev/null ：表示“黑洞”，一个空设备，所以进入到它里面的东西都会丢失
echo "hello" > t.log   可以写成  echo "hello" 1> t.log
这里的1，是文件描述符(df),文件描述符就是文件的下标。
<img src="E:\images\图片16.png" alt="图片16" style="zoom:80%;" />
文件描述符就是一个下标索引，所以这里的1，实际上表示stdout。

echo "hello" 1 > t.log  实际上完成的是stdout屏幕输出，重映射到t.log文件中   
nohup java -jar app.jar >log  2>&1  ：2>&1 表示的意思是2重映射到1，>&是一个整体，如果没有&，2>1表示的是将错误信息输入到1这个文件中。
nohup java -jar app.jar >log  2>&1 想让1重映射到app.jar上，然后让2重映射到1上，所以现在1和2都重映射到app.tar上了

--------------------

![image-20230817003643051](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20230817003643051.png)
各种$表示的含义。