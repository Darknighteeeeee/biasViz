import json


def calculate_lsm(file_a, file_b, output_file):
    """
    计算两个JSON文件中语言分类的LSM相似度并保存结果

    参数:
        file_a (str): 第一个JSON文件路径
        file_b (str): 第二个JSON文件路径
        output_file (str): 输出结果保存路径
    """
    try:
        # 加载JSON文件
        with open(file_a, 'r', encoding='utf-8') as f:
            data_a = json.load(f)

        with open(file_b, 'r', encoding='utf-8') as f:
            data_b = json.load(f)

        # 确保数据结构一致
        if not isinstance(data_a, dict) or not isinstance(data_b, dict):
            raise ValueError("输入JSON文件必须是字典格式")

        # 收集所有类别键（假设两个文件有相同的类别结构）
        all_categories = set(data_a.keys()).union(set(data_b.keys()))

        # 计算每个类别的LSM
        lsm_results = {}
        for category in all_categories:
            cat_a = data_a.get(category, 0)
            cat_b = data_b.get(category, 0)

            # 计算LSM
            numerator = abs(cat_a - cat_b)
            denominator = cat_a + cat_b + 0.0001  # 避免除以0
            lsm = 1 - (numerator / denominator)

            lsm_results[category] = round(lsm, 4)  # 保留4位小数

        # 保存结果
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(lsm_results, f, ensure_ascii=False, indent=4)

        print(f"LSM计算结果已保存到: {output_file}")
        return lsm_results

    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":
    # 替换为你的实际文件路径
    file1 = "project20_elite_programmers_features.json"
    file2 = "project20_non_elite_programmers_features.json"
    output = "lsm_results0.json"

    results = calculate_lsm(file1, file2, output)
    if results:
        print("计算结果:")
        print(json.dumps(results, indent=4, ensure_ascii=False))