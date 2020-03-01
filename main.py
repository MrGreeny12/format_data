import json
from pprint import pprint

with open('newsafr.json', encoding='utf-8-sig') as f:
    json_data = json.load(f)

# pprint(json_data)

# data = json_data['rss']['channel']
# # pprint(data)
#
# with open('chanel_content.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
#
# print('Выполнено')

import xml.etree.cElementTree as ET

tree = ET.parse('newsafr.xml')
root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)

items = root.findall('channel/item')
# print(items)

for item in items:
    print(item.find('description').text)
# print(items[1].find('description').text)