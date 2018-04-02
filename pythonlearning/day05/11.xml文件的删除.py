# Author:Louis Chu
import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):  #遍历这个根元素的所有的 year 模块
    new_year = int(node.text) + 1 #将这个模块的txt的属性加上1（首先哟转换成 int 类型）
    node.text = str(new_year) # 然后再转回字符串的类型
    node.set("updated_for", "louis") #新加一个属性

tree.write("xmltest.xml") #写入原来的文件

# 删除node
for country in root.findall('country'):  # 根文件中循环遍历country 这个xml标签
    rank = int(country.find('rank').text) #在每一个country 中找到里面的rank 标签
    if rank > 50: #如果rank>50  删除这个标签
        root.remove(country)

tree.write('output.xml') # 生成一个新的文件