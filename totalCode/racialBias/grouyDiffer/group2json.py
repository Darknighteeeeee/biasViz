import json
import os


def count_sentences(file_path):
    """统计文件中句子的数量（按行计算，假设每行是一个句子）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"警告: 文件 {file_path} 未找到，跳过统计")
        return 0


def process_projects(total_projects=20):
    """处理所有项目文件并统计句子数量"""
    project_stats = {}

    for project_num in range(1, total_projects + 1):
        # 构造文件名
        african_file = f"project{project_num}_african_english.txt"
        standard_file = f"project{project_num}_standard_english.txt"

        # 统计句子数量
        african_count = count_sentences(african_file)
        standard_count = count_sentences(standard_file)

        # 添加到统计字典
        project_stats[f"project{project_num}"] = {
            "african_english": african_count,
            "standard_english": standard_count,
            "total": african_count + standard_count
        }

    return project_stats


def save_to_json(data, output_file="sentence_statistics.json"):
    """将统计结果保存到JSON文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"统计结果已保存到 {output_file}")


if __name__ == "__main__":
    # 处理所有项目
    statistics = process_projects(20)

    # 保存到JSON文件
    save_to_json(statistics)

    # 可选：打印汇总信息
    total_african = sum(stats['african_english'] for stats in statistics.values())
    total_standard = sum(stats['standard_english'] for stats in statistics.values())
    grand_total = total_african + total_standard

    print("\n汇总统计:")
    print(f"所有项目的African English句子总数: {total_african}")
    print(f"所有项目的Standard English句子总数: {total_standard}")
    print(f"所有项目的句子总数: {grand_total}")