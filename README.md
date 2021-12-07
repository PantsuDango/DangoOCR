### 开头说明

​	   DangoOCR 是基于大家的 **CPU处理器** 来运行的，**CPU处理器 的好坏会直接影响其速度**，~~但不会影响识别的精度~~，目前此版本识别速度可能在 0.5-3秒之间，具体取决于大家机器的配置，可以的话尽量不要在运行时开其他太多东西。**需要配合团子翻译器 Ver3.6 及其以上的版本才可以使用！**

​       此项目底层基于百度开源的PaddleOCR搭建，这是团子第一次尝试自己封装离线的OCR，遇到了不少坑，也受到了不少人的帮助才顺利完成这第一个版本~此离线版本以后都会开源，团子也会慢慢优化它的精度和速度，也欢迎对OCR领域有所研究的大佬能一起讨论研究~

----



#### 项目相关

[DangoOCR 源码地址](https://github.com/PantsuDango/DangoOCR)  希望能收到你点的 Star ~ 团子感激不尽

ps：此文档为离线文档，相关说明和问题集可能会过时，如果此文档不能帮助你解决问题，请直接查看 [DangoOCR 源码地址](https://github.com/PantsuDango/DangoOCR) 



[团子翻译器 源码地址](https://github.com/PantsuDango/Dango-Translator)  配合翻译器 Ver3.6 及其以上版本使用，啃生肉！



[b站个人主页](https://space.bilibili.com/227927)  关于 团子翻译器 和 团子OCR 的任何事宜，团子都会第一时间在b站的动态发布，关不关注你看着办~



团子QQ：**394883561**               邮箱：**394883561@qq.com**



#### 特别鸣谢

[PaddleOCR 项目地址](https://github.com/PaddlePaddle/PaddleOCR)  项目底层基于此框架搭建



[QPT 打包工具地址](https://github.com/GT-ZhangAcer/QPT)  推荐开发者了解一下这个打包工具，比 pyinstaller 好用！DangoOCR 就是使用此工具打包的 ~ 感谢作者 

----



### 使用前注意

1. 只可以运行在 x64 位的系统，x86 32位的系统可以暂时不支持；
2. 只支持windows，windows7-10都可以，windows7以下不行，mac和移动端和linux都不支持；
3. 使用前务必关掉所有杀毒软件，不然被误杀导致文件缺失无法启动自己想办法；
4. <span style="color:red;">只可以运行在全英文的路径，路径中不能含有中文或者中文类型的字符；</span>
5. <span style="color:red;">路径不可以带有空格；</span>

~~以后的版本可能会修复以上问题~~，第4.5条注意事项可详见下图说明：

![image-20210704214037559](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704214037559.png)

#### **错误演示**

路径带的 "团子" ，有中文启动会失败

![image-20210701223423557](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223423557.png)

#### **正确演示**

![image-20210701224518547](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701224518547.png)

#### **特别说明**

对于盘符，D盘C盘E盘，盘符及其之前的路径带有中文是没有关系，不会影响的

![image-20210701224626396](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701224626396.png)



---



### 安装和启动

第一次启动需要初始化（安装），**切勿关闭黑色的运行窗口**，待进度条满后初始化完毕，只有第一次启动才会有进度条

![image-20210704212345901](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704212345901.png)



中途这些红色的错误不需要在意，不影响，等它一直运行就好了

![image-20210704212736642](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704212736642.png)



如弹出，点允许访问

![image-20210701223004058](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223004058.png)



出现如下情况，则启动完毕，可以配合翻译器直接使用了，<span style="color:red;">**使用过程中千万不可以关掉此运行的黑窗口，直接缩小即可**</span>

![image-20210701223025840](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223025840.png)



注意翻译器此处**不要打勾，不要打勾**，如果打勾就是使用百度的OCR，当然你有高额度的百度OCR账号优先用百度OCR会更好

![image-20210701235359751](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235359751.png)



----



### 测试工具

可以在不使用翻译器的情况下简单测试自己的 DangoOCR 是否正常

![image-20210701235626384](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235626384.png)



记得先完成 DangoOCR 的运行，再启动此脚本测试，可以测试使用速度

![image-20210701235640888](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235640888.png)



如图完成测试，团子的测试结果是平均 0.81s，垃圾CPU

![image-20210701235941050](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235941050.png)





### 已知的问题和解决方案

---

#### 计算机名中文

![image-20210704213040053](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213040053.png)

出现如上图的错误的话，按照如下方法解决：

![image-20210704213157922](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213157922.png)

错误是由于你的计算机名带有汉字或者一些奇葩字符导致的，需要修改成英文或者数字

![image-20210704213215736](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213215736.png)

修改完成后保存重启 DangoOCR 即可

![image-20210704213258783](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213258783.png)

---



#### 缺少vc++2017运行环境

![image-20210704213642176](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213642176.png)

安装以下文件即可解决

![image-20210704213853088](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704213853088.png)



---



#### 缺少 mkl 驱动

一些盗版系统或者老版系统可能会没有 mkl 驱动，DangoOCR 需要此驱动来加速 OCR 的识别速度

![image-20210704214127025](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704214127025.png)

[参考此链接文章处理](https://blog.csdn.net/qq_35133971/article/details/100101397)

需要的文件在这里

![image-20210704214251847](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210704214251847.png)

解压后都丢到 **C:\Windows\System32** 就可以解决了







