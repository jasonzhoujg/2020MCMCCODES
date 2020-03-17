import pandas as pd


microwave = pd.read_csv('inforweight_mic.csv')
scores =pd.read_csv('score.csv')

a = 0.8
b=0.2


review = scores.scores.values
ratings = scores.ratings.values
microwave['review_scores'] = 0
microwave['ratings_scores']=0
microwave['comprehensive_scores']=0.00

for i in range(len(review)):
    microwave.review_scores.values[i]=review[i]
    microwave.ratings_scores.values[i] = ratings[i]
    microwave.comprehensive_scores.values[i]=a*ratings[i]+b*review[i]


microwave.to_csv('inforweight_mic.csv')


print(review,ratings)
print(microwave)
