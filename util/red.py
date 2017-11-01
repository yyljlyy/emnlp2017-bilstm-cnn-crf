# coding=utf-8
import HTMLParser

import jieba


def read_data():
    """
    对要训练的文本进行处理，最后把文本的内容的所有词放在一个列表中
    """
    # 读取停用词
    stop_words = []
    with open('stop_words.txt', "r") as f:
        ls = f.readline()
        while ls:
            stop_words.append(ls[:-1])
            ls = f.readline()
    stop_words = set(stop_words)
    print('停用词读取完毕，共{n}个词'.format(n=len(stop_words)))

    # 读取文本，预处理，分词，得到词典
    raw_word_list = []
    with open('17-11-2.csv', "r") as f:
        line = f.readline()
        while line:
            html_parser = HTMLParser.HTMLParser()
            split = line.strip().split(",")
            if len(split) == 1:
                continue
            line = html_parser.unescape(split[1].replace(" ", "").decode("utf8"))
            if len(line) > 0:  # 如果句子非空
                print(line)
                raw_words = []
                for l in list(jieba.cut(line, cut_all=False)):
                    if l not in stop_words:
                        raw_words.append(l)
                raw_word_list.extend(raw_words)
            line = f.readline()

    return raw_word_list  # step 1:读取文件中的内容组成一个列表
words = read_data()
print('Data size', len(words))
with open("text8", "w") as wf:
    for w in words:
        wf.write(w.encode("utf8") + " ")