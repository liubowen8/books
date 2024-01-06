# docker

经过对计算机网络中DHCP等概念的学习。
现在看一下虚拟机中“桥接”，“NAT”，“仅主机”的区别
桥接：![图片4](E:\images\图片4.png)
虚拟机就像是要给真正的机器一样，和物理机处于平等的地位。
NAT：![图片5](E:\images\图片5.png)
创造了一个新的局域网，物理机在这个局域网中充当代理服务器的作用。
仅主机模式：
![图片6](E:\images\图片6.png)
相比于NAT模式，此时的物理机没有代理功能，只能在新建的那个局域网中通信。

--------------------

![31cc50e8f01802aadd74145f1bda648](E:\images\31cc50e8f01802aadd74145f1bda648.jpg)

```shell
-f  ： 是强制的意思
-d ： 是守护进程的意思，启动一个docker
-p ： 是映射
比如-p 100:200 ，这即是宿主机上的端口100，映射到容器的200端口。其实完整的抒写方式是 宿主机ip：100 → 容器id：200
-i ： 为docker打开标准输入
-t ： 为docker分配要给伪终端
-i的时候，docker可以进行标准输入了，但是在哪里进行输入呢？
所以需要一个-t，打开一个伪终端
-a ： all的意思
-c ： 意思是这个容器使用多少cpu权重
-m ： 意思是这个容器使用多少内存
-v ： 意思是挂载

--name ： 设置name属性
为什么有些参数前面是-，有些参数前面是--，这是因为它们属于不同的风格。我们可以简单的认为-a 是 --all的简写。

docker容器的迁移，docker容器的导入和导出
docker export -o xxx.tar 容器名/容器id 
-o 用来指定导出的文件名
这样就把容器打包到xxx.tar文件夹中了，可以把xxx.tar传到其他机器上，然后执行：
docker import xxx.tar 仓库：标签
这样就得到了一个镜像
```

docker的安装：
![图片9](E:\images\图片9.png)

```shell
docker search image  # 在镜像仓库中搜一下xxx
docker pull image # 从镜像仓库中把xxx拉过来
docker run -d -p 1234:80 image
-d 就是daemon的意思，意思是启动容器的守护进程
-p 端口映射，宿主机的1234映射到容器的80
只是-d，并不会进入到容器，只是启动了守护进程。
# 销毁容器
docker rm -f containerID
# 其实也可以进到容器里面 crtl+d 或者 exit 退出
-f  ： 是强制的意思
-d ： 是守护进程的意思，启动一个docker
-p ： 是映射
-i ： 为docker打开标准输入
-t ： 为docker分配要给伪终端
-i的时候，docker可以进行标准输入了，但是在哪里进行输入呢？
所以需要一个-t，打开一个伪终端
-a ： all的意思
```

镜像在磁盘上就是一系列文件的集合：
![图片10](E:\images\图片10.png)
docker默认的镜像存储路径是“/var/lib/docker”，docker的存储路径是可以更改的：

```shell
mkdir -p /data/docker
cd /etc/docker
vi daemon.json # 对daemon.json文件进行修改
systemctl daemon-reload
systemctl restart docker

“”“
在daemon.json文件中输入：
{“graph”: "/data/docker"} # 后面这个就是自定义的路径。
“”“
```

```shell
docker run --name liu -p 2206:3306 \
-e MYSQL_ROOT_PASSWORD=xxxxxx -d image
# --name liu 给容器起了一个名字
# -e 给容器传递变量的。
```

在pull拉取镜像时，如果速度较慢，可以配置国内的镜像源。书本P33。

*--------------------------------------------------------------------*

创建image，第一种方式：

```shell
docker commit containerID repository：TAG
# 缺点
# 1：只有生成镜像的人，知道执行过什么命令，别人无法得知
# 2：修改只发生在当前层，对之前层无法修改
```

第二种方式：dockerfile
docker build 的使用，每执行一句指令，就生成一个新的镜像，并最终输出最终的镜像ID。

```txt
FROM centos
RUN echo ’<h1>demo</h1>‘ > /usr/share/nginx/html/index.html
RUN mkdir /root/tools # mkdir也算是一个动作，也会生成一个新的镜像
COPY jdk.tar.gz /root/tools
# COPY是从宿主机copy到docker，docker上本来一无所有，所以docker之间文件的copy，都可以通过宿主机到docker的copy来完成。
ADD http://xxxx/bin/jdk.tar.gz /root/tools
# ADD 从网上下载压缩包，并放在/root/tools下
```

----------------

docker容器的迁移：
docker export -o xxx.tar  容器名/容器id  # 把容器就行打包，并把压缩包发到主机b
主机b： docker import xxx.tar 仓库：标签  # 在主机b上，把压缩包解压为镜像

-------------

docker资源控制：
docker本身在**默认情况下**并不会对容器使用的资源进行控制，如果一次使用多个容器的话，会造成宿主机自身资源不够用。
所以docker可以借助使用linux cgroup进行资源控制。
**cgroup本身可以实现对cpu、内存、IO带宽的控制：**可以使用cgroup设置cpu的使用阈值，限制应用访问系统内存，显示IO带宽（比如一个进程，被限制只可以使用20%cpu，64KB内存，IO带宽只有1MB/s），这些都是可以通过Linux cgroup来实现的。
**docker借助cgroup实现对cpu，内存，IO带宽的控制：**

```shell
docker run -it 镜像
docker run -it -c 512 镜像  
# -c 或者 --cpu-shares： 意思是cpu使用的权重，默认值为1024.所以这里一个容器使用1024权重的cpu，另一个容器使用512权重的CPU

#使用-m参数对内存进行限制
docker -it -m 256m 镜像 # 限制了容器只能只有256MB的内存
```

-----------

数据管理：
挂载：
docker run -it -v  path1:path2 --privileged=true 镜像 /bin/bash
--privileged=true ：使容器中的root，真正拥有root权限，成功完成挂载
path1在宿主机，path2在docker容器内，修改path1中的文件，path2中也会跟着修改，所以可以在宿主机上开发代码，在docker容器中运行代码。

--------------------

docker有四种网络通信模式：bridge，container，host 和 none

bridge：
![图片11](E:\images\图片11.png)
docker0是在宿主机上的。就是给这些容器创建一个局域网，docker0起到路由、DHCP的功能。这个局域网的子网网段是可以自定义的。
#自定义局域网bridge2：
docker network create -d bridge --ip-range=192.168.1.0/24  --gateway=192.168.1.1  --subnet=192.168.1.0/24  bridge2
docker run -it --network=bridge2 --ip=192.168.1.3 镜像 # 在bridge2的局域网中启动一个容器，并自定义它的ip地址

host：
容器和宿主机使用相同的IP和网络配置。所以他们之间可能存在对网络资源的竞争。
书中说，**此模式下宿主机和容器可以很容易的通过localhost或者127.0.0.1实现互相访问，这是如何进行的呢？**

container：
容器之间共享网络资源，一个容器使用另外一个容器的网络命名空间。容器之间可以使用localhost或者127.0.0.1实现互相访问。
docker run -it --network=container：容器id  镜像 /bin/bash

none：
容器具有独立的网络命名空间，但不包含任何网络配置，只能通过localhost或者127.0.0.1访问容器。（只有local loopback网卡）

--------------------

docker容器之间的通信具体方式：
同一个宿主机上的容器的通信方式：IP，dockerdnsserver，jointed
IP的方式： 直接使用容器的ip地址进行通信
dockerdnsserver：使用docker的name进行通信
jointed：容器之间使用container的通信模式，这样就可以使用127.0.0.1或者localhost进行通信了。

-----------

不同节点上的docker之间的通信（不同计算机上的docker之间的通信）
1）通过容器端口映射，使用宿主机进行转发
2）通过overlay，实现不同节点上容器的通信就像是一台宿主机节点通信一样，直接使用虚拟ip（最常用）
3）使用第三方网络实现容器间的跨节点通信
overlay：
overlay的实现需要注册中心的支持，注册中心有zookeeper，consul和etcd。
不同节点上容器之间的通信，可以使用zookeeper注册中心，将不同节点上的容器放在一个子网网段上，有点类似于vlan（虚拟局域网）。
本质上就是把不同节点上的容器拎出来，放在同一个局域网下。

-------

docker compose： 对复杂的任务进行编排

如果我们要实现一个应用，这个应用可能需要使用很多容器，容器之间需要相互交换数据，此时我们可以手动的一个一个的运行容器，但是这样比较麻烦，所以就有了compose
compose就是一个yaml文件，在文件中可以按照顺序写好先启动哪个容器，后启动哪个容器，然后使用dockor-compose up一键式启动这些容器。

默认的情况下，启动的这些容器是在同一个网段下的，每一个容器都使用容器名作为host，这是对容器的唯一标记，所以容器的名字要唯一。
当然对于每一个要启动的容器，也可以在compose的yaml文件中，设置自己的网络空间，每一个容器都可能来自于不同的子网网络（这也进一步佐证了，在一个宿主机上可以create多个局域网）

--------------

docker对代理的设置，以及本地host对代理的设置：
![图片13](E:\images\图片13.png)
对网络的代理只需要两步：
1：设置端口映射
2：需要上网的设备，连ip2，ip2会发给ip3，所以在此设备上要提供ip3的账号、密码。

---------

docker machine： 一个远程管理工具，
docker machine还提供了相应的命令以管理远端的docker环境
*-----------------------------------------------*
docker swarm：swarm是群的意思
把若干个宿主机抽象为一个整体，并通过一个入口统一管理这些宿主机上的各个docker（和docker machine的区别是一个是管理一个，一个是管理一群）

-----------------------------

docker基本命令：

```
docker images 查看本地镜像信息
```

```
docker run：
docker run -d -p 1234:80 镜像
-d 启动守护进程，此时会创建一个容器。 
-p 是完成映射，前面的是宿主机的端口，后面是容器的端口
 
```

```
docker ps
查看docker的容器信息
```

```
docker rm：
docker rm -f 容器ID ： 终止和销毁容器信息
```

