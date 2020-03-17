import pandas as pd




mircrowave = pd.read_csv('infor_mic.csv')
Vine_l = mircrowave.vine.values
Veri_l = mircrowave.verified_purchase.values
H_l = mircrowave.helpful_votes.values
P_l = mircrowave.total_votes.values
M_l= mircrowave.mutural_information.values
I_l= mircrowave.informationentropy.values

mircrowave['inforweight']=0.00000000




#计算信息量
# Vine = 0
# Veri = 1
# H =12
#
# P = 15
# I = 0
# M = 0
alpha = 0.01
belta = 10
gama = 0.1


for i in range(len(H_l)):
    Vine1 = Veri_l[i]
    P = P_l[i]
    I = I_l[i]
    H = H_l[i]
    Veri1 = Veri_l[i]
    M = M_l[i]

    if 'Y' in Vine1:
        Vine =1
    else:
        Vine = 0
    if 'Y' in Veri1:
        Veri=1
    else:
        Veri=0
    if P == 0:
        P=1

    if Vine ==0:
         Infor= (Veri+H/P)*(alpha*I+belta*M+gama*H)
    else:
        Infor= (Vine+H/P)*(alpha*I+belta*M+gama*H)

    mircrowave.inforweight.values[i] = Infor

mircrowave.to_csv('inforweight_mic.csv')

