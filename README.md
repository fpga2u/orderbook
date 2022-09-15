# AXOrderBook

A股订单簿工具，使用逐笔行情进行订单簿重建、千档快照发布、各档委托队列展示等，包括python模型和FPGA HLS实现。

---

## 订单簿（Order Book）及其重建

订单簿是某只交易标的在某一时刻买卖订单按价格档位组织而成的列表，常见的5档快照即是订单簿最优5档价格的切片。完整的订单簿包括所有存在有效订单的价格档以及每个价格档上的排队订单。

目前A股交易所（深交所、上交所）发布的L2行情快照仅发布10档快照及此10档的前50笔排队订单，若需要查看更多价格档或更多排队订单，则需要利用L2行情的逐笔委托和逐笔成交进行订单簿重建。

交易所发布的快照行情实时性较差，通常认为是3秒一次，只有使用逐笔行情进行订单簿重建才能看到实时行情，并重现整个标的的价格变化过程。

A股交易所L2行情相关背景参考：[交易所L2行情与撮合原理](/doc/SE.md)

> 订单簿重建算法

由于交易所会发布逐笔委托和逐笔成交消息，因此进行订单簿重建的思路至少有两种：模拟撮合和等待成交。

* 模拟撮合

    在收到逐笔委托后，就模拟交易所撮合机制进行成交判断并修改价格档位和订单队列，即刻生成新的订单簿。

    优势：更新订单簿的速度快；在集合竞价阶段也可以发布订单簿；可以发布价格档位的订单队列。

    劣势：为进行模拟撮合，必须按照价格和序列号（时间）两个维度来管理订单，数据结构复杂。

* 等待成交

    由于交易所的成交消息是紧跟在委托之后的，所以可在收到委托后先缓存，待收齐对应的成交消息后，根据成交内容修改价格档位和订单队列，从而生成新的订单簿。

    优势：不需要管理订单队列，数据结构简单。

    劣势：更新订单簿的速度有延时；集合竞价阶段不能重建订单簿；只能发布价格档、没有对应的订单队列。

我们试图同时实现两种方式，再在实机上进行互相比较。

---

## python 模型

我们首先会用python实现订单簿重建算法的模型，进行算法正确性和资源评估，之后在FPGA上用HLS实现。为了便于转换成HLS，python的实现会采用许多原始数据结构。

开发环境：

* windows 10 / Centos 8 stream

* Anaconda + python 3.8.10

---

## FPGA HLS实现

订单簿重建需要的算力过大，通常都是采用FPGA引擎卸载来加速。我们会在验证完python模型后用[Xilinx Vitis](https://www.xilinx.com/products/design-tools/vitis/vitis-platform.html)环境开发对应的FPGA HLS实现。

预计开发环境：

* Centos 8 stream

* Xilinx Vitis 2022.1

* Xilinx Alveo U50

* Xilinx pynq 2.6.2

---

## 参考资料

[点击跳转](/doc/reference.md)

---

## 数据源

我们从深交所某日的L2行情中截取了几只个股的行情消息，并格式化成易于阅读的和使用的二进制格式，可从以下地址下载后放置于[data目录](/data/)下：

链接：https://pan.baidu.com/s/13O7b30DXM64j4WpnNgvXXg 

提取码：rxif

---

## 预备工作

* 订单簿重建流程梳理

* HLS 链表工具和测试

* HLS AVL工具和测试

* HLS HBM工具和测试

* HLS 测试环境
