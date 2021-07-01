# "data" format should be allele lists of result from various tools  [2420,3303,2420,4404] 
# "hla" should be either "A","B" or "C"  (hla type)
# model_acc.csv = ( 100- accuracy rate) %


# Searching most frequent value

def frequent(list):
    count = 0
    no = list[0]
    for i in  list:
        current_freq = list.count(i)
        if (current_freq > count):
            count = current_freq
            num = i
            
    return num 



# Finding most frequent value location

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
      lis = data[res[-1]+1:]
    except:
      break     
  return res


# List of possible model combinations 

def comb(x):
    from itertools import combinations
    return list(combinations(x,2))


# Counting accuracy of models

import csv

def acc(x,y):
    content = list(csv.reader(open("model_acc.csv","rt",encoding='UTF8')))
    content.pop(0)
    parseContent = []
    for target in x:
        if (y.lower() == "a"):
            yIdx = 1 
        elif (y.lower() == "b"):
            yIdx = 2 
        elif (y.lower() == "c"):
            yIdx = 3 
        else:
            continue       
        parseContent.append(content[target - 1][yIdx])
    return parseContent


# Correlation value calling

def cor(x):
    content = list(csv.reader(open("cor_score.csv", "rt",encoding='UTF8')))
    content.pop(0)
    parseContent = []
    for target in x:
        parseContent.append(content[target[0]][target[1]+1])
    return parseContent


# Multipy values on the list 

from functools import reduce

def multiply(a):
    return reduce(lambda x, y: x * y, a)


# Calculation Weight
def calw(data,hla):
    weight= sum(list(map(float,cor(comb(find_index(data,frequent(data)))))))/len(cor(comb(find_index(data,frequent(data)))))
    weight2=weight**len(cor(comb(find_index(data,frequent(data)))))
    return weight2

#Multiplying models' accuracies

def calt(data,hla):
    arr = list(map(float,acc((find_index(data,frequent(data))),hla)))
    return multiply(arr)

# Calculation accuracy

def calc(data,hla):
    cal= calw(data,hla)*calt(data,hla)
    return cal

# Calling / you can set up threshold of percentage of acccuracy here, default:99.9999

def call(data,hla):

    if calc(data,hla)<0.0001:
        print(frequent(data))
    else:
        print('Recommended PCR-SBT')


        
