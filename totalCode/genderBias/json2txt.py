import json

# 读取 JSON 文件
with open('compute_liwc_ZeroNet.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 提取特定项
# name = data.get('name', '未找到name项')  # 使用 get 方法，如果 key 不存在则返回默认值
name = data[0]['text']
name1 = data[1]['text']
# 写入 TXT 文件
with open('output19.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(name + '/n')
    txt_file.write(name1)

print("提取完成，已写入 output2.txt 文件")