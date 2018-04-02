# Author:Louis Chu
import xml.etree.ElementTree as ET #导入的模块

new_xml = ET.Element("personInfolist") # 生成的根节点标签名称
# 创建一个 personInfolist 下面的标签 标签名称是 perisonInfo 里面的属性名是 enrolled 属性值是 yes
personInfo = ET.SubElement(new_xml, "personInfo", attrib={"enrolled": "yes"})
# 在 perisonInfo 下面创建标签 name 里面的文字是louis
name = ET.SubElement(personInfo, "name")
name.text = 'louis'

# 在 perisonInfo 下面创建标签 age 属性名是 checked  值是 no
age = ET.SubElement(personInfo, "age", attrib={"checked": "no"})
# 在 perisonInfo 下面创建标签 sex 里面的文字是  33
sex = ET.SubElement(personInfo, "sex")
sex.text = '24'

personInfo2 = ET.SubElement(new_xml, "personInfo", attrib={"enrolled": "no"})

# 在 perisonInfo 下面创建标签 name 里面的文字是louis
name = ET.SubElement(personInfo, "name")
name.text = 'louis'
age = ET.SubElement(personInfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("xml文件生成.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式