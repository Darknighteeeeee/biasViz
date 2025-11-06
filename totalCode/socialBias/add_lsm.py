import json

# 读取JSON文件
with open('lsm_results0.json', 'r') as file:
    data = json.load(file)

# 计算所有数值的平均值
values = list(data.values())
average = sum(values) / len(values)

# 添加LSM字段
data['lsm'] = round(average, 4)

# 将更新后的数据写回文件
with open('lsm_results0.json', 'w') as file:
    json.dump(data, file, indent=4)

print(f"已添加LSM字段，平均值为: {average}")
