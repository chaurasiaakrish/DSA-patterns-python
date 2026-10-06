# To return distinct indices whose sum is equal to the target sum where the array is given sorted
# Example: [1,1,2,2,3,3]

nums=[1,1,2,2,3,3]
target=4
i=0
j=len(nums)-1
l=[]
while(i<j):
    if nums[i]+nums[j]==target:
        l.append([nums[i],nums[j]])
        i+=1
        j-=1
    elif nums[i]+nums[j]>target:
        j-=1
    elif nums[i]+nums[j]<target:
        i+=1   
    while(nums[i]==nums[i-1]):
        i+=1
    while(nums[j]==nums[j+1]):
        j-=1                
print(l)    