# TinyPng

一个使用TinyPng提供的API，用于Windows或Mac端快速压缩图片的Python脚本，可以做到将该目录及子目录下所有的图片进行压缩，压缩之前可以指定备份地址，脚本会自动在压缩前备份原图

# 背景
 1.为了减小安装包体积，需要对项目里的图片进行压缩处理，使用tinypng官网处理的话比较麻烦，还需要上传文件夹并且下载已经压缩完的文件,然后再替换项目里的图片，操作起来比较麻烦，而本脚本文件可以直接一键压缩并替换，很方便。

# 注意事项

1. 本文编写的脚本目前在mac上运行正常，windows 系统上没有测试，如有问题可联系本人解决；
2. 如果是由于业务需求导致无法实现你想要的功能，您可以提issue，互相交流；
3. 如果你是免费用户，那么每个developer key最多只能压`500`次，可通过多注册几个邮箱的方式解决次数的限制。

# 使用教程

1. 安装Python，Mac系统自带，Windows电脑可通过[官网](https://www.python.org/downloads/)下载；
2. 在终端或CMD窗口中输入`python -V`命令，校验Python是否正确安装；
3. 在终端或CMD窗口中输入`pip install -i https://pypi.doubanio.com/simple/ tinify`命令，使用国内镜像下载安装tinify；
4. 先进入[TinyPng官网](https://tinypng.com/)登录用户，接着进入[TinyPng Developers](https://tinypng.com/dashboard/developers)网址后选择`Developer API`，然后复制Developer API Key；
5. 在终端或CMD窗口中输入`MMBang_ImageCompression_v2.0`或`MMBang_ImageCompression_v2.0`命令，进行图片批量压缩；

有任何问题可以添加本人微信交流：15802178512
