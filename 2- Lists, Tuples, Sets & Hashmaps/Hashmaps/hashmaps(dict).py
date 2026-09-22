# Creation of dictionary
freq={}

# Insertion / Updation 
freq["a"]=freq.get("a",0)+1

# Read
print(freq)  # Output: {'a': 1}

# Deletion 
freq["a"]-=1

# Delete if not exist 
if freq["a"]==0:
    del freq["a"]

# No. of distinct characters
print(len(freq))      # Output: 0

# Exercise  Count the characters in the string given as s

s= "aabbcab"
dic={}
for value in s:
    dic[value]=dic.get(value,0)+1

print(dic) # {'a': 3, 'b': 3, 'c': 1}
print(len(dic))    # 3

# Alternative Method without using .get()

l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
print(l)
