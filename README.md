### 开头说明

​	   DangoOCR 是基于大家的 **CPU处理器** 来运行的，**CPU处理器 的好坏会直接影响其速度**，~~但不会影响识别的精度~~，目前此版本识别速度可能在 0.5-3秒之间，具体取决于大家机器的配置，可以的话尽量不要在运行时开其他太多东西。**需要配合团子翻译器 Ver3.6 及其以上的版本才可以使用！**

​       此项目底层基于百度开源的PaddleOCR搭建，这是团子第一次尝试自己封装离线的OCR，遇到了不少坑，也受到了不少人的帮助才顺利完成这第一个版本~此离线版本以后都会开源，团子也会慢慢优化它的精度和速度，也欢迎对OCR领域有所研究的大佬能一起讨论研究~

[DangoOCR 源码地址](https://github.com/PantsuDango/DangoOCR)  希望能收到你点的 Star ~ 团子感激不尽

[团子翻译器 源码地址](https://github.com/PantsuDango/Dango-Translator)  配合翻译器 Ver3.6 及其以上版本使用，啃生肉！

[b站个人主页](https://space.bilibili.com/227927)  关于翻译器的任何事宜，团子都会第一时间在b站的动态发布，希望能得到你的关注~



#### 特别鸣谢

[PaddleOCR 项目地址](https://github.com/PaddlePaddle/PaddleOCR)  项目底层基于此框架搭建

[QPT 打包工具地址](https://github.com/GT-ZhangAcer/QPT)  推荐开发者了解一下这个打包工具，比 pyinstaller 好用！DangoOCR 就是使用此工具打包的 ~ 感谢作者 





### 使用前注意

<span style="color:red;">目前 DangoOCR 只可以运行在全英文的路径，路径带有中文会报错，</span>~~以后的版本会修复此问题~~，见下图说明：

#### **错误演示**

路径带的 "团子" ，有中文启动会失败

![image-20210701223423557](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223423557.png)

#### **正确演示**

![image-20210701224518547](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701224518547.png)

#### **特别说明**

对于盘符，D盘C盘E盘，盘符及其之前的路径带有中文是没有关系，不会影响的

![image-20210701224626396](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701224626396.png)



### 安装和启动

第一次启动需要初始化（安装），切勿关闭黑色的运行窗口，待进度条满后初始化完毕，只有第一次启动才会有进度条

![image-20210701222858629](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701222858629.png)



如弹出，点允许访问

![image-20210701223004058](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223004058.png)



出现如下情况，则启动完毕，可以配合翻译器直接使用了，<span style="color:red;">**使用过程中千万不可以关掉此运行的黑窗口，直接缩小即可**</span>

![image-20210701223025840](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701223025840.png)



注意翻译器此处**不要打勾，不要打勾**，如果打勾就是使用百度的OCR，当然你有高额度的百度OCR账号优先用百度OCR会更好

![image-20210701235359751](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235359751.png)



### 测试工具

可以在不使用翻译器的情况下简单测试自己的 DangoOCR 是否正常

![image-20210701235626384](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235626384.png)



记得先完成 DangoOCR 的运行，再启动此脚本测试，可以测试使用速度

![image-20210701235640888](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235640888.png)



如图完成测试，团子的测试结果是平均 0.81s，垃圾CPU

![image-20210701235941050](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210701235941050.png)