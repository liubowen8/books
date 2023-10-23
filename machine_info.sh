echo "---------机器型号和序列号--------------"
dmidecode | grep "Product Name"
sudo dmidecode | grep "System Information" -A9 | egrep "Manufacturer|Product|Serial"
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"

echo "---------操作系统内核型号--------------"
uname -a
echo "怎么看内核型号的"
echo "以 Linux dfee-agent08 3.10.0-1160.66.1.el7.x86_64 #1 SMP Wed May 18 16:02:34 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux 为例："
echo "dfee-agent08 ： 表示主机名"
echo "3.10.0-1160.66.1.el7.x86_64 内核主版本号为3，次版本号为10，修订版本号为0，第1160次修改，el7表示是redhat enterprise linux 7 → #1 SMP Wed May 18 16:02:34 UTC 表示第1次编译和编译的时间 "
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"

echo "---------操作系统发行版型号--------------"
uname -m && cat /etc/*release 
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"
echo "---------主板信息--------------"
dmidecode -t 2
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"
echo "---------CPU--------------"
echo "--------- CPU型号--------------"
lscpu
echo "---------CPU物理个数--------------"
cat /proc/cpuinfo |grep "physical id" | sort | uniq | wc -l
echo "---------单个CPU核数--------------"
cat /proc/cpuinfo| grep "cpu cores"| uniq
echo "---------CPU逻辑数--------------"
cat /proc/cpuinfo| grep "processor"| wc -l
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"

echo "---------每一个内存条的型号--------------"
sudo dmidecode -t memory | grep -e Type
echo "---------每一个内存条的容量--------------"
sudo dmidecode -t memory | grep -e Size
echo "---------每一个内存条的读取速度--------------"
sudo dmidecode -t memory | grep -e Speed
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"

echo "---------各个磁盘和分区--------------"
lsblk
echo "这里的type字段会看到lvm，这个东西和disk、part有区别，lvm表示 Linux Volume Manager 卷管理器，使用Lvm会生成dm-n逻辑卷，dm的意思是device mapper，完成从逻辑设备到物理设备的映射"
echo "在查询到disk之后，使用：cat /sys/block/sda/queue/rotational 查询sda这个disk是不是SSD，如果输入为0，表示这个磁盘不rotation，不旋转，所以是SSD磁盘"
echo "0 → 不旋转 → SSD固态硬盘；   1 → 旋转 → HDD机械硬盘"
lsblk -d -o name,rota
echo "查看硬盘的接口信息： SAS 、 SATA、 Nvme"
cat /proc/scsi/scsi
echo "***********************************************************************************************************"
echo "-----------------------------------------------------------------------------------------------------------"
echo "***********************************************************************************************************"
echo "---------网卡信息-------"
lshw -class network
echo "这种方式有些网卡看不到网速，所以 ethtool 网卡逻辑名  的方式查看网卡的网速"
