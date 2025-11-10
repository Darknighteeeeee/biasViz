import numpy as np
import math

# 加载GloVe词向量
def load_glove_model(glove_file):
    print("Loading GloVe Model...")
    model = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            vector = np.array([float(val) for val in split_line[1:]])
            model[word] = vector
    print(f"Done. {len(model)} words loaded!")
    return model

    # with open(glove_file, 'r', encoding='utf-8') as file:
    #     for line in file:
    #         try:
    #             # 分割行，此时由于词汇内部可能有空格，所以不能直接使用 split()
    #             # 我们可以先按任意数量的空格分割，然后再处理词汇部分
    #             parts = line.strip().split(None, 1)  # 这里使用 split(None, 1) 是为了只分割一次，得到词汇和其余部分
    #             if len(parts) < 2:
    #                 # 如果分割后没有足够的部分，说明这行格式不正确，可以跳过
    #                 print(f"Skipping malformed line: {line.strip()}")
    #                 continue
    #
    #             # 去除词汇内部的空格
    #             word = ''.join(parts[0].split())
    #
    #             # 获取向量部分并转换为 NumPy 数组
    #             vector_str = parts[1]
    #             vector = np.array([float(val) for val in vector_str.split()])
    #
    #             # 将处理后的词汇和向量添加到模型中
    #             model[word] = vector
    #         except ValueError as e:
    #             # 如果在转换向量时遇到错误，打印错误信息并跳过当前行
    #             print(f"Error parsing vector for word '{parts[0].strip()}': {e}")
    #             continue
    # return model

# 计算余弦相似度
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

# 计算欧几里得距离
def euclidean_distance(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)

# 主函数
def main():
    glove_file = 'vectors1.txt'  # 修改为你的GloVe文件路径
    model = load_glove_model(glove_file)

    word_man1 = 'he'
    word_man2 = 'his'
    word_man3 = 'him'
    word_man4 = 'guys'
    word_man5 = 'man'
    word_girl1 = 'she'
    word_girl2 = 'her'



    word_bao1 = 'excellent'
    word_bao2 = 'better'
    word_bao3 = 'good'
    word_bao4 = 'pretty'
    word_bao5 = 'nice'
    word_bian1 = 'bad'
    word_bian2 = 'worse'
    word_bian3 = 'ugly'
    word_bian4 = 'wrong'
    word_bian5 = 'error'

    # if word_man1 in model and word_bao2 in model:
    #     vec1 = model[word_man1]
    #     vec2 = model[word_bao2]
    #
    #     cos_sim = cosine_similarity(vec1, vec2)
    #     eucl_dist = euclidean_distance(vec1, vec2)
    #
    #     print(f"Cosine Similarity between '{word_man1}' and '{word_bao1}': {cos_sim}")
    #     print(f"Euclidean Distance between '{word_man1}' and '{word_bao1}': {eucl_dist}")
    # else:
    #     print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")
    #


    #整合向量整体计算
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_girl2 in model and word_bao1 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec8 = model[word_girl2]
        vec7 = model[word_bao1]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)



        print(f"Cosine Similarity between '{word_man1}' and '{word_bao1}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bao1}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bao1}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bao1}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bao1}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bao1}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bao1}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bao1}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bao1}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bao1}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bao1}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bao1}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bao1}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bao1}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bao2 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec8 = model[word_girl2]
        vec7 = model[word_bao2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)



        print(f"Cosine Similarity between '{word_man1}' and '{word_bao2}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bao2}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bao2}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bao2}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bao2}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bao2}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bao2}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bao2}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bao2}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bao2}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bao2}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bao2}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bao2}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bao2}': {eucl_dist6}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bao3 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec8 = model[word_girl2]
        vec7 = model[word_bao3]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bao3}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bao3}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bao3}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bao3}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bao3}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bao3}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bao3}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bao3}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bao3}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bao3}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bao3}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bao3}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bao3}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bao3}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bao4 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec8 = model[word_girl2]
        vec7 = model[word_bao4]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bao4}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bao4}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bao4}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bao4}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bao4}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bao4}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bao4}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bao4}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bao4}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bao4}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bao4}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bao4}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bao4}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bao4}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bao5 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec8 = model[word_girl2]
        vec7 = model[word_bao5]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bao5}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bao5}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bao5}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bao5}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bao5}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bao5}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bao5}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bao5}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bao5}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bao5}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bao5}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bao5}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bao5}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bao5}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bian1 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec7 = model[word_bian1]
        vec8 = model[word_girl2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bian1}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bian1}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bian1}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bian1}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bian1}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bian1}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bian1}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bian1}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bian1}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bian1}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bian1}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bian1}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bian1}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bian1}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bian2 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec7 = model[word_bian2]
        vec8 = model[word_girl2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bian2}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bian2}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bian2}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bian2}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bian2}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bian2}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bian2}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bian2}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bian2}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bian2}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bian2}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bian2}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bian2}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bian2}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")

    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bian3 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec7 = model[word_bian3]
        vec8 = model[word_girl2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bian3}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bian3}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bian3}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bian3}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bian3}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bian3}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bian3}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bian3}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bian3}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bian3}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bian3}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bian3}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bian3}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bian3}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")



    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bian4 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec7 = model[word_bian4]
        vec8 = model[word_girl2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bian4}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bian4}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bian4}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bian4}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bian4}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bian4}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bian4}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bian4}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bian4}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bian4}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bian4}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bian4}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bian4}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bian4}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")


    print("--------------------------------------------------------------")
    if word_man1 in model and word_man2 in model and word_man3 in model and word_man4 in model and word_man5 in model and word_girl1 in model and word_bian5 in model:
        vec1 = model[word_man1]
        vec2 = model[word_man2]
        vec3 = model[word_man3]
        vec4 = model[word_man4]
        vec5 = model[word_man5]
        vec6 = model[word_girl1]
        vec7 = model[word_bian5]
        vec8 = model[word_girl2]

        cos_sim1 = cosine_similarity(vec1, vec7)
        eucl_dist1 = euclidean_distance(vec1, vec7)

        cos_sim2 = cosine_similarity(vec2, vec7)
        eucl_dist2 = euclidean_distance(vec2, vec7)

        cos_sim3 = cosine_similarity(vec3, vec7)
        eucl_dist3 = euclidean_distance(vec3, vec7)

        cos_sim4 = cosine_similarity(vec4, vec7)
        eucl_dist4 = euclidean_distance(vec4, vec7)

        cos_sim5 = cosine_similarity(vec5, vec7)
        eucl_dist5 = euclidean_distance(vec5, vec7)

        cos_sim6 = cosine_similarity(vec6, vec7)
        eucl_dist6 = euclidean_distance(vec6, vec7)

        cos_sim7 = cosine_similarity(vec8, vec7)
        eucl_dist7 = euclidean_distance(vec8, vec7)

        print(f"Cosine Similarity between '{word_man1}' and '{word_bian5}': {cos_sim1}")
        print(f"Euclidean Distance between '{word_man1}' and '{word_bian5}': {eucl_dist1}")

        print(f"Cosine Similarity between '{word_man2}' and '{word_bian5}': {cos_sim2}")
        print(f"Euclidean Distance between '{word_man2}' and '{word_bian5}': {eucl_dist2}")

        print(f"Cosine Similarity between '{word_man3}' and '{word_bian5}': {cos_sim3}")
        print(f"Euclidean Distance between '{word_man3}' and '{word_bian5}': {eucl_dist3}")

        print(f"Cosine Similarity between '{word_man4}' and '{word_bian5}': {cos_sim4}")
        print(f"Euclidean Distance between '{word_man4}' and '{word_bian5}': {eucl_dist4}")

        print(f"Cosine Similarity between '{word_man5}' and '{word_bian5}': {cos_sim5}")
        print(f"Euclidean Distance between '{word_man5}' and '{word_bian5}': {eucl_dist5}")

        print(f"Cosine Similarity between '{word_girl1}' and '{word_bian5}': {cos_sim6}")
        print(f"Euclidean Distance between '{word_girl1}' and '{word_bian5}': {eucl_dist6}")

        print(f"Cosine Similarity between '{word_girl2}' and '{word_bian5}': {cos_sim7}")
        print(f"Euclidean Distance between '{word_girl2}' and '{word_bian5}': {eucl_dist7}")
    else:
        print(f"One or both words ({word_girl1}, {word_bao1}) not found in the GloVe model.")


if __name__ == "__main__":
    main()