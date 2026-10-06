# To move zeroes to the last 
# Eg: [1,0,0,2,3] becomes [1,2,3,0,0]

def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

nums = [1,0,0,2,3]
moveZeroes(nums)
print(nums)