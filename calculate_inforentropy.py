import pandas as pd
from math import log2


#信息熵计算公式

microwave = pd.read_excel('microwave1.xlsx')
review_title = microwave.review_headline
review_body = microwave.review_body


review = review_title+review_body
review = review.values
# review_list = review.split()


fre = pd.read_excel("mircrowave.csv")
fre_list = fre.fre.values
word_list = fre.word.values
microwave['informationentropy']=0.0000000
Infor = microwave.informationentropy.values
# print(sum(fre_list))
# print(fre.word.values)
# I = 0
T = sum(fre_list)
# Infor = []
for i in range(len(review)):
    s = review[i].split()
    I=0
    for j in range(len(s)):
        if s[j] in word_list:
            P = fre_list[i]/T
            I = -P*log2(P) +j
        pass
    Infor[i]=I
    print(i)


for i in range(len(review)):
    Infor[i] = microwave.informationentropy.values[i]

microwave.to_csv('infor_mic.csv')




# #计算信息量
# Vine = 0
# Veri = 1
# H =12
#
# P = 15
# I = 0
# M = 0
# alpha = 1
# belta = 1
# gama = 1
#
#
# if Vine ==0:
#      Infor= (Veri+H/P)*(alpha*I+belta*M+gama*H)
# else:
#     Infor= (Vine+H/P)*(alpha*I+belta*M+gama*H)
#
# print(Infor)
#
# #计算评论评级
#
# weight = pd.read_excel('featureword.xlsx')
# weight_list = weight.weight.values
# weight_name = weight.word.values
# flag = 0
# values = 0
# for i in range(len(review_list)):
#     if review_list[i] in weight_name:
#         for j in range(len(weight_name)):
#             if weight_name[j] == review_list[i]:
#                 flag =flag +1
#                 values = values +weight_list[j]
# if flag ==0:
#     results =round(3)
# else:
#     results = values/flag
#
# print(round(results))






#计算互信息，首先看每个星级出现的概率，之后根


# #计算权重部分
# #init
# review = "I have a dream one day"
# ratings= 3
#
# #加载文件
#
# word_weiht = pd.read_excel("")
# weightlist = word_weiht.weight.values
# review_list = review.split
#
# for i in range(len(review_list)):
#     pass
#

