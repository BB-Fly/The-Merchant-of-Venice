# 文本格式转换与统计

## 任务描述

本任务利⽤正则表达式解析给定的《The Merchant of Venice》HTML⽹⻚文件，并将文件内容按Markdown格
式存储⾄文件中，同时把统计结果写入文件中。

## 功能实现函数介绍

1. 辅助功能函数
```python
str_find(s:str,target:str,idx:int)->int
''' 在字符串s中，从索引为idx的位置开始寻找target子串，返回找到的子串索引位置。
    查找失败时返回-1
'''

```

2. MD子任务函数
``` python
get_list_scene(file_path:str)->list
''' 在file_path路径文件中，寻找子文件路径字符串，并以列表形式返回。
'''

get_scene_script(file_path:str,act_list:list)->str
''' 将file_path路径的html文件内容按照转换规则转换成MD文件格式，并返回字符串文本。
'''

write_script(file_name:str, content:str)->None
''' 将context字符串续写在file_name路径对应的文件后。
'''

get_MD(file_path="data/Merchant of Venice_ List of Scenes.html",targetpath="document/venice.MD")
''' 完整的MD子任务实现函数
'''

```

3. tag子任务函数
``` python
get_scene_tag_dict(file_path:str)->dict
''' 统计file_path路径下html文件中的tag数量，以map：str->int 的字典形式返回
'''

get_TAG(file_path="data/Merchant of Venice_ List of Scenes.html",targetpath="document/venice.tag")
''' 完整的tag子任务实现函数
'''

```


至2022/11/28，测试无误