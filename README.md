# Graduation Project
***
> the data come from [REDD site]

[REDD site]:http://redd.csail.mit.edu

use svm to make a Classifier which can Classify a device's on/off from the total circuit of home



```
readme.txt

----------
低频功率数据
----------
low_freq/
目录包含各电源线和房子的电路的平均功率读数（这也包含具有单独插头的房屋的插头负载显示器）。
房子的数据以大约每秒一次的频率记录
电路每三秒钟一次

文件目录组织如下：

REDD / low_freq /
  house_ {1..n} / - 每个房子的目录
    labels.dat - 每个通道的设备类别标签
    channel_ {1..k} .dat - 每个通道的时间/瓦特数读数

主目录由几个house_i目录组成
每个目录都是单个房屋的所有功率读数
每个房子子目录由一个labels.dat和几个channels_i.dat组成
标签文件包含线路号和文本标签指示此通道上设备的类别
例：

1 mains_1
2 mains_2
3 refrigerator
4 lighting
...

在电路上有多个设备类型的情况下，最好按电路的主要类型分类。

每个channel_i.dat文件：
UTC时间戳（作为整数） 功率读数（记录电路的视在功率）
...
1306541834      102.964
1306541835      103.125
1306541836      104.001
1306541837      102.994
1306541838      102.361
1306541839      102.589
...
```
