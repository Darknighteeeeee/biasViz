# import liwc
# import re
# from collections import Counter
# parse, category_names = liwc.load_token_parser('LIWC2007_English100131.dic')
#
#
# def tokenize(text):
#     # you may want to use a smarter tokenizer
#     for match in re.finditer(r'\w+', text, re.UNICODE):
#         yield match.group(0)
#
#
# gettysburg = '''Four score and seven years ago our fathers brought forth on
#   this continent a new nation, conceived in liberty, and dedicated to the
#   proposition that all men are created equal. Now we are engaged in a great
#   civil war, testing whether that nation, or any nation so conceived and so
#   dedicated, can long endure. We are met on a great battlefield of that war.
#   We have come to dedicate a portion of that field, as a final resting place
#   for those who here gave their lives that that nation might live. It is
#   altogether fitting and proper that we should do this.'''.lower()
# gettysburg_tokens = tokenize(gettysburg)
# gettysburg_counts = Counter(category for token in gettysburg_tokens for category in parse(token))
# print(gettysburg_counts)

import liwc
import re
from collections import Counter
from pathlib import Path
import json
import os

# 加载LIWC解析器
parse, category_names = liwc.load_token_parser('LIWC2015 Dictionary.dic')
projectNum = 1
pro_num = 20

def tokenize(text):
    """简单的分词函数，将文本分割为单词"""
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)


def analyze_liwc(file_path):
    """分析文本文件的LIWC特征"""
    # 读取文件内容
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"文件 {file_path} 不存在")

    text = file_path.read_text(encoding='utf-8').lower()

    # 分词并分析
    tokens = tokenize(text)
    counts = Counter(category for token in tokens for category in parse(token))

    return counts


def calculate_features(results):
    """
    计算LIWC特征
    :param results: LIWC分析结果字典
    :return: 包含计算特征的字典
    """
    features = {
        'ppron': results['ppron'],
        'ipron': results['ipron'],
        'article': results['article'],
        'prep': results['prep'],
        'auxverb': results['auxverb'],
        'adverb': results['adverb'],
        'conj': results['conj'],
        'negate': results['negate'],
        'affect': results['affect'],
        'analytic_thinking': (results['ppron'] + results['ipron'] + results['article'] + results['prep'] +
                              results['auxverb'] + results['adverb'] + results['conj'] + results['negate'] +
                              results['affect']),
        'authentic': (results['i'] + results['shehe'] + results['they'] + results['negemo'] +
                      results['differ'] + results['motion']),
        'clout': (results['i'] + results['we'] + results['you'] + results['negate'] +
                  results['social'] + results['differ'] + results['swear']),
        'tone': (results['posemo'] + results['negemo'])
    }
    return features


def save_to_json(data, filename):
    """
    将数据保存到JSON文件
    :param data: 要保存的数据
    :param filename: 文件名
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_results(elite_results, non_elite_results, elite_features, non_elite_features):
    """
    保存分析结果和特征到JSON文件
    """
    # 保存原始LIWC计数结果
    save_to_json(elite_results, 'project' + str(pro_num) + '_elite_programmers_liwc_counts.json')
    save_to_json(non_elite_results, 'project' + str(pro_num) + '_non_elite_programmers_liwc_counts.json')

    # 保存计算特征
    save_to_json(elite_features, 'project' + str(pro_num) + '_elite_programmers_features.json')
    save_to_json(non_elite_features, 'project' + str(pro_num) + '_non_elite_programmers_features.json')
def cal_lsm(cata,catb):
    """
    :param cata: category a
    :param catb: category b
    :return: lsm
    """

# 示例用法
if __name__ == "__main__":

    # 读取 JSON 文件
    with open('compute_communication/compute_liwc_aframe.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # 提取特定项
    # name = data.get('name', '未找到name项')  # 使用 get 方法，如果 key 不存在则返回默认值
    name = data[0]['text']
    name1 = data[1]['text']
    directory = 'corpus_group'
    # 写入 TXT 文件
    with open(os.path.join(directory, 'project' + str(pro_num) + '_elite.txt'), 'w', encoding='utf-8') as txt_file:
        txt_file.write(name)

    with open(os.path.join(directory, 'project' + str(pro_num) + '_unelite.txt'), 'w', encoding='utf-8') as txt_file1:
        txt_file1.write(name1)

    print("提取完成，已写入 output2.txt 文件")
    # 你可以替换为任何txt文件路径
    file_to_analyze1 = "corpus_group/project" + str(pro_num) + "_elite.txt"  # 精英人群语料库
    file_to_analyze2 = "corpus_group/project" + str(pro_num) + "_unelite.txt"  # 非精英人群语料库

    try:
        results = analyze_liwc(file_to_analyze1)
        results1 = analyze_liwc(file_to_analyze2)

        # 计算特征
        elite_features = calculate_features(results)
        non_elite_features = calculate_features(results1)

        # 保存结果
        save_results(results, results1, elite_features, non_elite_features)

        # 8 + 4
        # 3 9 10 11 12 13 14 15
        ppron = results['ppron']
        ipron = results['ipron']
        article = results['article']
        prep = results['prep']
        auxverb = results['auxverb']
        adverb = results['adverb']
        conj = results['conj']
        negate = results['negate']
        analytic_thinking = (results['ppron']+results['ipron']+results['article']+results['prep']+results['auxverb']
                             + results['adverb']+results['conj']+results['negate']+results['affect'])
        authentic = results['i']+results['shehe']+results['they']+results['negemo']+results['differ'] + results['motion']
        clout = results['i']+results['we']+results['you']+results['negate']+results['social']+ results['differ']+results['swear']
        tone = results['posemo'] + results['negemo']
        # print(clout)
        # print(authentic)
        # print(tone)
        # print(analytic_thinking)

        ppron1 = results1['ppron']
        ipron1 = results1['ipron']
        article1 = results1['article']
        prep1 = results1['prep']
        auxverb1 = results1['auxverb']
        adverb1 = results1['adverb']
        conj1 = results1['conj']
        negate1 = results1['negate']
        analytic_thinking1 = (results1['ppron'] + results1['ipron'] + results1['article'] + results1['prep'] + results1['auxverb']
                    + results1['adverb'] + results1['conj'] + results1['negate'] + results1['affect'])
        authentic1 = (results1['i'] + results1['shehe'] + results1['they'] + results1['negemo']
                      + results1['differ'] + results1['motion'])
        clout1 = (results1['i'] + results1['we'] + results1['you'] + results1['negate'] + results1['social'] + results1['differ']
                  + results1['swear'])
        tone1 = results1['posemo'] + results1['negemo']
        # print(results['ppron']+results['ipron']+results['article']+results['prep']+results['auxverb']
        #       + results['adverb']+results['conj']+results['negate']+results['affect'])
        print(results)
    except FileNotFoundError as e:
        print(e)