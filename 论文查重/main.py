
import jieba #用于中文的分词
import numpy as np #用于方便进行计算
import string
import sys
from line_profiler import LineProfiler
num=0
stopwordlist = []

def cos_dist(vec1,vec2):
    #用于计算余弦相识度
    dist1=float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    #dot是对传入两个数组进行向量的内积计算
    #linalg.norm是对两向量进行平方和的平方根计算
    return dist1

def remove_punctuation(text):#用于去除标点符号
    translator=str.maketrans("","",string.punctuation)#去除所有的标点符号
    return text.translate(translator)#将创建的字符转换成文本

def remove_stopwords(text,stopwordist):#用于将文本中的停用词进行删除
    words = jieba.cut(text)
    filter_words=[word for word in words if word not in stopwordist]
    return " ".join(filter_words)

def stopword_cut(stopwordlist):
    stopword = [r"D:\python\pythontxt\论文查重\baidu_stopwords.txt",r"D:\python\pythontxt\论文查重\cn_stopwords.txt",r"hit_stopwords.txt"]
    #读取停用词,获得停用词列表
    #stopwordlist = []#这里是将所有的停用词进行读取到stopwordlist上,方便后序进行文字的分割
    for eachfile in stopword:
        with open(eachfile,'r',encoding='utf-8') as f:
            stopwordlist.extend([word.strip('\n') for word in f.readlines()])
    return stopwordlist

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "文件不存在。"

def write_to_text_file(content,put_outpath):
    c=put_outpath

    file1=c

    try:
        with open(file1, 'w', encoding='utf-8') as file:
            file.write(content)
            file.write("\n")
        print(f"内容已成功写入 {c} 文件。")
    except Exception as e:
        print(f"写入文件时出现错误：{e}")

def write_to_text_file1(content,put_outpath):
    c = put_outpath
    file1 = r"c"
    try:
        with open(file1, 'a', encoding='utf-8') as file:
            file.write(content)
            file.write("\n")
        print(f"内容已成功写入 {file1} 文件。")
    except Exception as e:
        print(f"写入文件时出现错误：{e}")
def delet(file_path):#用于判断是否前面加了"和后面加了",然后删除它
    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]
    return file_path

def creat_vector(file_content,file_content1):
    file1 = remove_stopwords(remove_punctuation(file_content), stopwordlist)
    file2 = remove_stopwords(remove_punctuation(file_content1), stopwordlist)
    key_word = list(set(file1 + file2))
    # 创建两个向量,并对其进行初始化
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))
    for i in range(len(key_word)):
        for j in range(len(file1)):
            if key_word[i] == file1[j]:
                word_vector1[i] += 1
        for k in range(len(file2)):
            if key_word[i] == file2[k]:
                word_vector2[i] += 1
    return word_vector1,word_vector2
def put_out(file_path1,file_path2,c,put_outpath):
    global num
    combine_text="查重文件路径:   " + file_path1+"\n" + "对比文件路径:   " + file_path2+"\n" + "查重的文件与特定文件的相似度为:    " + str(c)
    if num==0:
        write_to_text_file(combine_text,put_outpath)
        num+=1
    else :
        write_to_text_file1(combine_text,put_outpath)



def pass_function(file_content,file_path1,put_outpath):
    file_path1 = delet(file_path1)
    file_content1 = read_file(file_path1)  # file_content1作为读取的需要比较的文本
    word_vector1, word_vector2 = creat_vector(file_content, file_content1)
    c = cos_dist(word_vector1, word_vector2)
    c = round(c, 2)
    put_out(file_content, file_path1, c,put_outpath)

def main():
    global stopwordlist
    if len(sys.argv) > 1:
        file_path = sys.argv[1]  # 原文文件
        file_path1 = sys.argv[2]  # 抄袭文件
        put_outpath = sys.argv[3]  # 答案文件
    else:
        print("没有提供文件位置参数")
    file_content = read_file("file_path")  # file_content作为读取的需要进行查重的文本
    stopwordlist = stopword_cut(stopwordlist)  # 创建出停用词列表
    pass_function(file_content, "file_path1", "put_outpath")

if __name__=="__main__":
    lp = LineProfiler()#构建分析函数
    lp.add_function(cos_dist)
    lp.add_function(remove_punctuation)
    lp.add_function(remove_stopwords)
    lp.add_function(stopword_cut)
    lp.add_function(read_file)
    lp.add_function(write_to_text_file)
    lp.add_function(delet)
    lp.add_function(creat_vector)
    lp.add_function(put_out)
    lp.add_function(pass_function)
    test_func=lp(main)
    lp.print_stats()
    main()


