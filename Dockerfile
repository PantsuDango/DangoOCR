FROM centos:7

ENV LANG=en_US.utf8

# 安装依赖环境
RUN yum update
RUN yum -y install gcc
RUN yum -y install zlib-devel
RUN yum -y install bzip2-devel
RUN yum -y install openssl-devel
RUN yum -y install ncurses-devel
RUN yum -y install sqlite-devel
RUN yum -y install readline-devel
RUN yum -y install tk-devel
RUN yum -y install gdbm-devel
RUN yum -y install libpcap-devel
RUN yum -y install xz-devel
RUN yum -y install libffi-devel
RUN yum -y install make
RUN yum -y install mesa-libGL.x86_64

# 安装python
RUN cd /usr/local
RUN curl -O https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
RUN tar -zxvf Python-3.7.0.tgz && rm -f Python-3.7.0.tgz
RUN mkdir /usr/local/python37
RUN cd Python-3.7.0
RUN ./configure --prefix=/usr/local/python37
RUN make && make install
RUN cd /usr/local && rm -rf /usr/local/Python-3.7.0
RUN ln -s /usr/local/python37/bin/python3.7 /usr/bin/python3
RUN ln -s /usr/local/python37/bin/pip3.7 /usr/bin/pip3
RUN pip3 install --upgrade pip

# 安装PaddleOCR
RUN pip3 install paddlepaddle
RUN pip3 install "paddleocr==2.0.6"

RUN mkdir -vp /data && cd /data
WORKDIR /data
RUN curl -O http://39.108.110.77/group1/default/20210624/12/19/5/33745153e1c36c0de5743b3318f07df9.py
RUN mv 33745153e1c36c0de5743b3318f07df9.py ocr_test.py
RUN curl -O http://39.108.110.77/group1/default/20210624/12/21/5/bc77a06529e648b5c89620bf352c5360.jpg
RUN mv bc77a06529e648b5c89620bf352c5360.jpg image.jpg
RUN curl -O http://39.108.110.77/group1/default/20210624/14/47/5/9858569826b7ac479e031c89b70fc216.24
RUN mv 9858569826b7ac479e031c89b70fc216.24 libstdc++.so.6.0.24 && chmod +x libstdc++.so.6.0.24
RUN mv libstdc++.so.6.0.24 /usr/lib64/
RUN cd /usr/lib64/ && rm -f libstdc++.so.6 && ln -s libstdc++.so.6.0.24 libstdc++.so.6

CMD["/bin/bash"]