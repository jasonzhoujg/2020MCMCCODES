import pandas as pd

def Delwords(str):
    stop_exl = pd.read_excel('stoplist.xlsx')
    # print(stop_list)
    stop_list = stop_exl.list.values


    for i in range(len(stop_list)):
        if stop_list[i] in str:
            str = str.replace(stop_list[i], "")
    return str

txt=open('test.txt')

wordlist = []
dict = {}
# dict={'aa':100}
# dict['bb']=0
# print(dict)
readl = txt.readline()
j =0
while readl:
    context = str(readl)
    context = Delwords(context)
    lines = context.split()
    for i in range(len(lines)):
        if lines[i] in wordlist:
            dict[lines[i]] = dict[lines[i]]+1
        else:
            dict[lines[i]]=1
            wordlist.append(lines[i])
    readl = txt.readline()
    j = j +1
    print('have finished '+str(j)+'st liens')


df = pd.DataFrame(dict,index=['word'])
df = df.T
df.to_csv('mircrowave.csv')


