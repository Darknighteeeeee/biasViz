from transformers import pipeline
from tqdm import tqdm

# 加载 zero-shot 分类器模型
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# 候选标签
candidate_labels = ["African English", "Standard English"]

# 读取留言文件（每行一条留言）
with open("D:\pythondemo\pythonProject\liwc-python\corpus_group1\project4.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# 用于分类存储
african_english = []
standard_english = []

# 对每条留言进行判断
for line in tqdm(lines, desc="分类中"):
    result = classifier(line, candidate_labels)
    top_label = result["labels"][0]
    score = result["scores"][0]

    if top_label == "African English":
        african_english.append(line)
    else:
        standard_english.append(line)

# 写入结果到两个文件
with open("project4_african_english.txt", "w", encoding="utf-8") as f:
    for comment in african_english:
        f.write(comment + "\n")

with open("project4_standard_english.txt", "w", encoding="utf-8") as f:
    for comment in standard_english:
        f.write(comment + "\n")

print(f"分类完成 ✅\n非洲英语留言数：{len(african_english)}\n标准英语留言数：{len(standard_english)}")
