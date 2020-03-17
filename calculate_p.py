import pandas as pd
import numpy as np
from math import log2

Scores = pd.read_csv('score.csv')
mircrowave = pd.read_csv('hah.csv')

scores = Scores.reviews.values
ratings = Scores.ratings.values

d_scr = {}
d_rt = {}
name = []
for i in range(len(scores)):
    if scores[i] in name:
        d_scr[scores[i]] = d_scr[scores[i]] + 1
    else:
        d_scr[scores[i]] = 1
        name.append(scores[i])

name = []


for i in range(len(ratings)):
    if ratings[i] in name:
        d_rt[ratings[i]] = d_rt[ratings[i]] + 1
    else:
        d_rt[ratings[i]] = 1
        name.append(ratings[i])
print(d_scr)
print(d_rt)
# sum_src = sum(d_scr)
# sum_rt = sum(d_rt)
sum_src=0
sum_rt = 0

for j in range(5):
    sum_src = d_scr[j+1]+sum_src
    sum_rt = d_rt[j+1] + sum_rt


P_scr = []
P_rt = []

for j in range(5):
    P_rt.append(d_rt[j+1]/sum_rt)

for j in range(5):
    P_scr.append(d_scr[j+1]/sum_src)

P_t = []

list = np.zeros(25)

for i in range(len(scores)):
    a = scores[i]
    b = ratings[i]
    order =5*a+b-6

    list[order]=list[order]+1


P_t = list/sum_rt




print(P_t)
#互信息熵计算
M=np.array([])
mircrowave['mutural_information']=0.0000000000000
print()
for i in range(len(scores)):
    A=scores[i]
    B=ratings[i]
    mircrowave.mutural_information.values[i]= round(P_t[5*A+B-6]*log2(P_scr[A-1]*P_rt[B-1]/P_t[5*A+B-6]),10)






mircrowave.to_csv('infor_mic.csv')



# print(P_scr,P_rt)



