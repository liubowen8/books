# pod的概念

![image-20240109000744267](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20240109000744267.png)
一个pod中可能有多个容器，pod中可能有一个pause的容器。其他的容器共享pause容器的网络栈和存储卷。

# 自主性的pod

自主性的pod，pod退出后，并不会重建

# 控制器管理的pod

## RC： replication controller：副本控制器，用来控制pod的数量维持在一个期望值上

## RS： replicaset ： 比RC的优点在于：可以通过pod的label来批量处理pod，支持集合式selector

## Deployment ： 管理RS的。（RS不支持滚动更新。Deployment支持滚动更新。）

![image-20240109002127654](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20240109002127654.png)
Deployment创建RS， RS创建pod； 在滚动更新时，Deployment又创建一个RS-1，然后RS管理的pod逐渐退出，RS-1逐渐创建新版本的pod



## HPA： horizontal  pod  autoscaling 水平pod自动伸缩

![image-20240109002832610](C:\Users\Bowen\AppData\Roaming\Typora\typora-user-images\image-20240109002832610.png)
创建pod，相当于增加了工作的机器，可以缓解CPU利用率。HPA有最少和最多pod数量的设置。



## StatefulSet

1：稳定的持久化存储：相对于docker内部创建的文件，在docker退出之后文件就没了

2：稳定的网络标识： 重建后有相同的podname和hostname， ip地址也是相同的

3：有序部署、有序删除： pod的部署有顺序，比如有A和B两个pod，必须先创建A，再创建B。 先删除B再删除A。



## DaemonSet

在没有污点的node上运行pod；  在没有污点的所有的节点上面有启动一个pod



## Job

负责批处理任务，仅执行一次，保证pod成功结束：

保证pod成功结束 →  pod异常退出，Job会重新拉起pod，重新执行，直到pod成功退出。



## cronJob

给Job添加时间属性，比如周期性在给定的时间点运行Job