## FOR MAXIMUM SUM ofrom a subarray
i=0
summ=0
max_sum=0
nums=[]
while i<len(nums):
    summ=summ+nums[i]
    max_sum=max(max_sum,summ)
    if summ>0:
        i+=1
    else:
        summ=0
        i+=1
print(max_sum)        


## FOR MINIMUM SUM ofrom a subarray
i=0
summ=0
min_sum=0
nums=[]
while i<len(nums):
    summ=summ+nums[i]
    min_sum=min(min_sum,summ)
    if summ<0:
        i+=1
    else:
        summ=0
        i+=1
print(min_sum) 