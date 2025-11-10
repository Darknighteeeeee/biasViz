def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())

african_count = count_lines("project7_african_english.txt")
standard_count = count_lines("project7_standard_english.txt")
print(african_count + standard_count)
print(f"分类完成 ✅\n非洲英语留言数：{african_count}\n标准英语留言数：{standard_count}")