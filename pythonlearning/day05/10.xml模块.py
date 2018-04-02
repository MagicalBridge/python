# Author:Louis Chu
import xml.etree.ElementTree as ET #导入xml模块

tree = ET.parse("xmltest.xml") #解析要处理的程序
root = tree.getroot()
print(root);  # <Element 'data' at 0x00B86960> 打印的是xml的文件的内存地址
print(root.tag); # data 打印的根节点的标签名称

# 遍历xml文档
for child in root: # 遍历的是第一层的 孩子标签
    print(child.tag, child.attrib) # 打印出来第一层的孩子标签的名称 和 孩子标签的属性
    for i in child: # 再对孩子标签的进行遍历
        print(i.tag, i.text) #打印出孙子标签的标签标签名称 和相应的文字


# country
# {'name': 'Liechtenstein'}
# rank
# 2
# year
# 2008
# gdppc
# 141100
# neighbor
# None
# neighbor
# None
# country
# {'name': 'Singapore'}
# rank
# 5
# year
# 2011
# gdppc
# 59900
# neighbor
# None


# 只遍历year 节点 （这是遍历指定的标签） iter 指定的标签的名称
for node in root.iter('year'):
    print(node.tag, node.text)


# year 2008
# year 2011