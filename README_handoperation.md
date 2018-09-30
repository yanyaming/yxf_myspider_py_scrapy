yxf_myspider_py_scrapy : 环境配置手动操作内容
=========================================================
（已包含在自动脚本的配置：1.更新软件源；2.开启防火墙端口；3.安装c/c++编译器gcc；4.安装服务）  
------------

### 项目维护:
使用git版本控制，开发环境为linux虚拟机（centos7，与服务器环境相似，安装中文输入法用于更新文档），所有开发以及git的更新完全在此系统进行，git项目根目录/opt/yxf_myspider_py_scrapy，爬虫服务器根目录/opt/yxf_myspider_py_scrapy/myspider。  

### 上传到服务器:
VPS服务商vultr提供的centos系统默认关闭selinux，如此才能实现通过ssh远程登录，以及sftp远程文件。  
上传到同一位置/opt。  
上传后把所有的目录及文件设置模式为777：chmod 777 -R path  
第一次上传后使用项目中的脚本安装环境，后续上传只更新爬虫内容。  

### os:
关闭SELinux严格安全模式（累赘，若开启则服务软件很难拿到足够权限）：  
/etc/selinux/config：  
SELINUX=enforcing 改为 SELINUX=disabled  

### mongodb:

	  
### scrapy:


### shadowsocks:
需要提前修改配置文件的IP到服务器的公网IP，以及密码。  
其余全部通过脚本完成  
