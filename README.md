# biasViz

Quantify and visualize biases in open-source software projects

## 项目结构

项目的核心代码位于 totalCode 目录下，主要包含以下几个功能模块：

* socialBias/：社会偏见分析相关代码
* racialBias/：种族偏见分析相关代码
* genderBias/：性别偏见分析相关代码
* compute\_communication/：沟通内容计算相关数据文件
* totalCoding/：总体编码及分析结果文件

## 功能说明

##### 社会偏见分析（socialBias)

该模块主要基于 LIWC（Linguistic Inquiry and Word Count）工具对文本进行分析，以量化文本中的社会偏见相关特征。

**核心文件：**

* usage.py：LIWC 分析的主程序，包含文本分词、LIWC 特征提取、特征计算和结果保存等功能
* corpus\_group/：存放用于分析的文本语料库，区分精英人群和非精英人群的语料
* lsm\_fianl/、lsm\_result\_partner/：存放 LIWC 分析结果的 JSON 文件

**主要功能：**

* 加载 LIWC 词典并解析文本
* 对精英和非精英人群的语料进行对比分析
* 计算多个语言特征（如代词使用、情感倾向等）
* 将分析结果保存为 JSON 格式

##### 种族偏见分析 (racialBias)

该模块使用零样本分类模型对文本进行分类，以检测种族相关的语言特征。

**核心文件：**

* grouyDiffer/7.py：使用 Hugging Face 的 transformers 库加载分类模型，将文本分类为 "African English" 和 "Standard English"
* grouyDiffer/statistic.py：统计文本文件的行数

##### 性别偏见分析 (genderBias)

该模块通过词向量计算来分析性别相关词汇与评价词汇之间的关联，以检测性别偏见。

**核心文件：**

cos\_dis\_cal.py：计算性别相关代词与褒贬词汇之间的余弦相似度和欧氏距离

json2txt.py：将 JSON 格式的文本数据转换为 TXT 文件

**结果文件 (totalCoding)**

存放各类分析的结果文件，主要是 LSM（Language Style Matching）相关的计算结果，如lsm\_results0.json、lsm\_results7.json等。

## 使用方法

* 社会偏见分析：运行 socialBias/usage.py，程序会读取语料库文件，进行 LIWC 分析，并将结果保存为 JSON 文件
* 种族偏见分析：运行 racialBias/grouyDiffer/7.py，对文本进行分类并统计结果
* 性别偏见分析：运行 genderBias/cos\_dis\_cal.py，计算词汇间的相似度和距离，分析性别偏见

## 依赖库

* liwc：用于文本的 LIWC 分析
* transformers：用于加载和使用预训练的语言模型
* tqdm：用于显示程序运行进度
* json：用于处理 JSON 格式数据
* re：用于正则表达式处理
* collections：用于计数等数据处理

## 注意事项

* 运行相关代码前请确保已安装所需依赖库
* 社会地位偏见功能运行需要LIWC 2015 dictionary的支持



