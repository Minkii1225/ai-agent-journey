# 写一个"文本分析器"：统计字符频率、单词数、替换敏感词
text_str = input("请输入文本内容：")
# 统计字符频率
char_freq = input("请输入要统计的字符：")
print("字符频率统计：", text_str.count(char_freq))
# 统计单词数
word_count = len(text_str.split())
print("单词数统计：", word_count)
print("单词列表：", text_str.split())
# 替换敏感词
sensitive_words = input("请输入要替换的敏感词（用逗号分隔）：").split(",")
for word in sensitive_words:
    text_str = text_str.replace(word, "*" * len(word))
print("替换敏感词后的文本：", text_str)
