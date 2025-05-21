# 使用说明
## labelCloud
  
labelCloud为标注文件工具  
子文件夹pointclouds用于存放需要标注的bin文件  
labels为标签文件存放位置  

**值得注意：** 第一次创建类别和大小进行标注时，仅会生成 JSON 文件。创建完成后，重启工具即可自动生成对应的 text 标签文件。

## veloparser-master

这是激光雷达生成的pcap文件转Pcd文件的脚本，内还包含pcd文件转bin文件脚本

**值得注意：** 转bin文件脚本涉及到pypcd库使用，这里需要下载指定python3.版本，否则报错。


# 引用
感谢以下作者作出的贡献，本套件仅供参考学习使用。

veloparser：https://github.com/ArashJavan/veloparser.git

labelCloud：https://github.com/ch-sa/labelCloud.git
