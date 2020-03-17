import pandas as pd
from math import log2
import math
from pandas import Series
import matplotlib.pyplot as plt

weight = pd.read_excel('featureword.xlsx')
weight_list = weight.weight.values
weight_name = weight.word.values

microwave = pd.read_excel('microwave1.xlsx')
review_title = microwave.review_headline
review_body = microwave.review_body


review = review_title+review_body
review = review.values
# print(review)


# review_list = review.split()
# print(review_list)
fre = pd.read_excel("mircrowave.csv")
fre_list = fre.fre.values
word_list = fre.word.values


flag = 0
values = 0
review_ratings = []

for k in range(len(review)):

    review_list = review[k].split()
    flag=0
    values = 0
    for i in range(len(review_list)):
        if review_list[i] in weight_name:
            for j in range(len(weight_name)):
                if weight_name[j] == review_list[i]:
                    flag =flag +1
                    values = values +weight_list[j]

    if flag == 0:
        results = 3.0
    else:
        # results = round((values / flag)-0.1)
        results =values/flag
        # results =str(results)


    review_ratings.append(results)



d = {}
name = []


for i in range(len(review_ratings)):
    if review_ratings[i] in name:
        d[review_ratings[i]] = d[review_ratings[i]]+1
    else:
        d[review_ratings[i]] = 1
        name.append(review_ratings[i])


print(d)

h = microwave.star_rating.values
review_ratings = pd.DataFrame(review_ratings,h,columns=['scores'])

# X = range(100)
# # plt.plot(X,int(review_ratings))
# plt.scatter(X,h[0:100])
# plt.scatter(X,review_ratings[0:100])
#
# plt.show()

# microwave = pd.DataFrame(review_ratings,microwave)
# microwave.to_csv('test.csv')

review_ratings.to_csv("score_new.csv")

# print(review_ratings)
# if flag ==0:
#     results =3
# else:
#     results = values/flag
# print(round(results))