# "data" format should be allele lists of result from various tools  [2420,3303,2420,4404] 


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

# Counting number of frequent value

def count(x):
    return x.count(frequent(x))


# Calling the value if 6 values are same or specific 5 values are same

def calling(data):
    if count(data)>=6:
            print (frequent(data))        
    else:
        if find_index(data,frequent(data))==[0,1,2,5,6]:
            print (frequent(data))
        else:
            print ('Recommended PCR-SBT')
