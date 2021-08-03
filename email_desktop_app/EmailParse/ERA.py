import sys

from PyQt5.QtWidgets import QApplication

from EmailParse.logic.MainWindown import EmailWindown


if __name__ == '__main__':
	email_app = QApplication(sys.argv)
	window = EmailWindown()
	window.show()
	sys.exit(email_app.exec_())

"""
	1、config
	2、liguiyang 邮箱测试
	3、liguiyang
	
	
yum remove docker \
           docker-client \
           docker-client-latest \
           docker-common \
           docker-latest \
           docker-latest-logrotate \
           docker-logrotate \
           docker-engine
3.安装依赖设置yum仓库

安装依赖:
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

设置仓库:

yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
4. 安装docker

yum install docker-ce docker-ce-cli containerd.io
5. 启动并加入开机启动

systemctl start docker
systemctl enable docker
6.验证是否安装成功

docker version
docker run hello-world
显示如下即安装成功!

[root@iZ2ze68ge5c1uwlkmnb9ixZ zcapp]# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete
Digest: sha256:0e11c388b664df8a27a901dce21eb89f11d8292f7fca1b3e3c4321bf7897bffe
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
 
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash
 
Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/
 
For more examples and ideas, visit:
 https://docs.docker.com/get-started/

————————————————
版权声明：本文为CSDN博主「逆袭的小学生」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/q610376681/article/details/90483576
"""







