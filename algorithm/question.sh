mysql
left join / right join

Hadoop 不了解

Linux shell 不熟

docker 接触过



月底/暑假/偏算法：








# part1: hdfs文件存储
# 1. hdfs读写过程
# 答案: https://blog.csdn.net/whdxjbw/article/details/81072207

# part2: Mysql
CREATE EXTERNAL TABLE `ids`(
  `id` string)
COMMENT 'This is the ids table for xukui1'
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://ns1018/user/jd_ad/ads_create/xukui1/idsdir'
TBLPROPERTIES (
  'COLUMN_STATS_ACCURATE'='true',
  'mart_name'='jd_ad',
  'numFiles'='1',
  'numRows'='0',
  'rawDataSize'='0',
  'totalSize'='87913552',
  'transient_lastDdlTime'='1579507516')
# 1. 说一说数据库三范式
  #第一范式：要求有主键，并且要求每一个字段原子性不可再分
  #第二范式：要求所有非主键字段完全依赖主键，不能产生部分依赖
  #第三范式：所有非主键字段和主键字段之间不能产生传递依赖
# 2. inner join 和 left join 区别
# 3. 事务的4个特性、隔离级别
# 4. 介绍一下索引是什么？有几种？优缺点？
#https://blog.csdn.net/liutong123987/article/details/79384395/
# 5. B树和B+树的区别？为什么不使用哈希索引？b树是个什么数据结构?
# 6. HashMap的实现原理？
# 7. MYSQL存储引擎Innodb相关问题？
# 8. MySQL的优化有没有了解过？比如对模糊查询的优化
# 9. 建立索引的考虑因素（使用频率、联合索引、索引顺序）
# 10. 关系型数据库和非关系型数据库的区别？
# 11. 结构化数据库，半结构化数据库，非结构化数据库的区别？
# 12. 使用过视图吗？
# 13. 表级锁和分级锁的区别，在高并发中怎么体现？
# 14. 聚簇索引、覆盖索引与回表查询
# 15. 索引失效的情况，如何知道索引是否被用到
# 16. 什么是事务，事务并发带来的问题（脏读、不可重复读、幻读）
# 17. sql：4个人比赛的所有组合
# 18. sql：行转列问题
base client 通信协议
# part3: Spark
# 1. Spark的算子有哪些？懒加载？哪些算子会有shuffle过程？
  # spark算子：https://blog.csdn.net/Fortuna_i/article/details/81170565?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-10.vipsorttest&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-10.vipsorttest
  # action/transformation:https://blog.csdn.net/helloxiaozhe/article/details/78481784
  # shuffle算子：https://blog.csdn.net/gegeyanxin/article/details/85038525
# 2. Spark的shuffle过程？
#https://blog.csdn.net/zhanglh046/article/details/78360762
# 3.spark和mr的区别
#https://blog.csdn.net/lipviolet/article/details/88621034
# 4. flink和spark流计算的区别
#https://blog.csdn.net/weixin_40247263/article/details/97000109?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-10.vipsorttest&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-10.vipsorttest
# 5. job、stage、task的关系
#https://blog.csdn.net/mys_35088/article/details/80864092
# 6.Spark任务提交方式和执行流程
#https://www.cnblogs.com/frankdeng/p/9301485.html
# 7. spark shuffle和mr shuffle的区别及优化
#https://blog.csdn.net/u011110301/article/details/106341114
# 8. spark容错机制
#https://blog.csdn.net/dengxing1234/article/details/73613484
# 9. sparkSQL的几种join实现
#http://www.jobplus.com.cn/article/getArticleDetail/46975
# 10. 介绍下spark streaming
#https://blog.csdn.net/qq_37142346/article/details/80290868?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.vipsorttest&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.vipsorttest
# 11. spark RDD的理解
#https://blog.csdn.net/u011094454/article/details/78992293

# part4: Hive
# 1. 数据仓库的分层
# https://www.cnwebe.com/articles/102149.html
#https://www.cnblogs.com/itboys/p/10592871.html
# 2. 星型模型和雪花模型的选择
#https://zhuanlan.zhihu.com/p/139656253
# 3. 数据仓库和传统数据库的区别
#https://blog.csdn.net/lisi1129/article/details/54907130
# 4. 接上问，维度冗余及三范式
# 5. hive数据存储格式、压缩格式，区别
#https://www.cnblogs.com/skyl/p/4740301.html
#http://www.ccblog.cn/69.htm
#https://www.cnblogs.com/skyice/p/10459345.html
# 6. HQL执行慢是怎么解决的


# part5: Hadoop
# 1. hadoop组件
# 2. yarn监控
# 3. mapreduce的过程,shuffle过程
# 4. Hive中的UDF、UDTF、UDAF的区别是什么？
#https://blog.csdn.net/wyqwilliam/article/details/84500578
# 5. WordCount在MapReduce中键值对变化
# 6. hiveSQL怎么执行
# 7. 数据仓库的架构
#https://www.jianshu.com/p/78696e1a2b0e
# 8. 建立数据仓库中遇到的问题，怎么解决
# 9. 为什么block=128M？增大缩小有什么影响？
# 10. 数据倾斜问题产生的原因有哪几种，怎么解决？
# 11. hive内部表和外部表的区别
#https://my.oschina.net/u/4101357/blog/3198326
# 12. Hive调优
#https://zhuanlan.zhihu.com/p/80718835
# 13. mapreduce和hdfs是一体的吗，有什么关系
# 14. mapreduce有几种join
#https://blog.csdn.net/sofuzi/article/details/81265402
# 15. Hadoop的HA
# 16. zookeeper了解吗，能完整叙述下zookeeper启动和容错的选举流程吗？

# part6. 数据仓库
# 1. 你采集日志数据的时候是按照实时流采集的还是按照批次采集的？
# 2. 除了一道sql题，要求使用窗口函数
# 3. 数仓理论，分层，结合业务
# 4. 事实表怎么建的？周期快照表？对于缓慢维怎么处理的？

# part7. Hbase
# 1. hbase为什么很快

# part8. Flink
# 1. spark streaming和flink的比较（小米）
# 2. flink的状态（小米）
# 3. flink的容错机制、状态一致性（阿里）
# 4. 讲述一致性检查点的实现——分布式快照（阿里）
# 5. flink的watermark、窗口机制、时间（小米）
# 6. flink的运行构架

# part9: Redis
# 1. redis的优缺点
# 2. redis的数据类型
# 3. 为什么redis效率高
# 4. redis主从复制过程
# 5. AOF、RDB的优缺点、适用场景
# 6. redis的过期淘汰策略
# 7. 缓存雪崩、缓存击穿及如何解决
# 8. BIO、NIO、AIO区别，原理是什么，有哪些实现，我说redis是NIO
# 9. redis poll、epoll，持久化，缓存一致性怎么实现
# 10. redis集群搭建，投票容错机制、高可用等等，redis问了蛮多，其实还有像事务，消息队列，除了五种数据结构其他的，redis模块等

# part10. Python语法
# 1. python中list和tuple的底层异同点
# 2. python中Gil了解吗

# part11. 操作系统
# 1. 公平锁和非公平锁
# 2. 操作系统，进程线程区别
# 3. 死锁，四个必要条件
# 4. 解决死锁的方法
# 5. 银行家算法
# 6. 如何判断安全
# 7. 举一个属性不可分的例子
# 8. 可执行文件在Linux上的执行流程
# 9. 内存不够用了交换虚拟地址空间哪一块区域？
# 10. 如果调用的是swap怎么执行
# 11. 数据库模糊查询like怎么优化
# 12. 线程调度算法
# 13. 同进程的线程切换和不同进程间线程切换有什么区别
# 14. 什么情况下多核间产生线程调度
# 15. 协程由谁调度

# part12. Java
# 1. java虚拟机内存模型
# 2. 如何实现多线程
# 3. cap原则
# 4. 消息队列（不会）
# 5. 进程和线程区别
# 6. java虚拟机内存模型中，线程和进程会如何分配这些资源
# 7.  链表和数组在存储空间上的灵活性，增删改查哪个快
# 8. 平衡二叉树和b树区别
# 9. AUC是什么，有什么意义，怎么画出roc曲线
# 10. 算法题：矩阵最小路径和问题
# 11. 4种线程池功能
# 12. 场景题：如何测试出你处理大规模数据时，开多少个线程数是比较合适的，请设计一个方案。
# 13. Java中list,set,map的区别？
# 14. ArrayList, LinkedList, HashMap的底层结构？
# 15. 内存溢出和内存泄漏的区别？
# 16. 虚拟机中的垃圾回收器有哪些，对应的原理介绍？
# 17. 垃圾回收算法

# part13. kafka
# 1. kafka建立了几个broker、几个副本
# 2. kafka的数据存储在磁盘但是为什么速度依旧很快？有没有研究过？有没有研究过0拷贝技术。
# 3. 项目中的业务表都有哪些，这些表主要分为哪几类，它们是怎么关联的
# 4. zookeeper的选举机制，选举哪个节点的决定性因素有没有节点的启动时间、节点编号的大小等因素？
# 5. 如何选出Linux的所有进程中，CPU使用率最多的前三个进程？假如这些信息只有三列，如何用命令取出第二列？
# 6. 假设一个磁盘空间还有10个G，但是现在写数据却写不进去了，这可能是因为什么？

# part14. ES
# 1. ES为什么要用前缀树做索引
# 2. 前缀树能做的B+树也能做，跳表也能做，为什么不用其他数据结构？前缀树最大的亮点是什么？
# 3. ES为什么不能在原索引上修改？如果要在原索引上修改如何实现？

# part15. Kafka
# 1. kafka的文件存储机制
# 2. kafka的可靠性保障
#   1）生产者往broker发送消息（副本数据同步策略、ISR、ACK）
#   2）topic分区副本
#   3）leader选举
# 3. kafka一致性保障
# 4. 如何保障数据有序性
# 5. kafka和传统消息队列的区别

# part16: 网络协议
# 1. 访问一个网址会经过哪些步骤
#https://www.cnblogs.com/xuebf/p/10837090.html
# 2. tcp/udp协议
# 3. http哪层?
# 4. 如何把UDP变的安全可靠
# 5. 拥塞窗口，慢启动，快重传，快恢复
# 6. RPC是什么，和restful的http有什么区别，什么场景下使用，socket和他们有什么关系
# 7. dubbo默认使用什么传输协议？mina和netty知道吗？
# 8. 为什么TCP建立连接时要三次握手，而不是两次握手；为什么TCP关闭连接时，要四次握手，而不是三次握手。
# 9. TCP里面的拥塞控制、滑动窗口、流量控制、冷启动

# part17. 数据结构
# 1. 时间复杂度，空间复杂度
# 2. 堆排序的原理以及数据结构
# 3. 数组和链表区别
# 4. 数据结构都有哪些

# part18. Linux命令
# 1. sed grep awk
# 2. 多线程和多进程的优缺点
# 3. 进程和线程的区别
# 4. 进程通信、线程通信
# 5. 为什么一个线程崩溃后其他线程会受影响
# 6. 常见的远程通信框架有什么？远程通信协议有哪些？序列化协议、传输方式？动态代理有几种？