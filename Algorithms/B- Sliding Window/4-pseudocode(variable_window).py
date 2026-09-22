class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        low = 0
        high = 0
        res = float("inf")  # minimium to be find therefore initializing res with the max possible no.(NULL)
        summ = 0
        length = 0
        # main variable window pseudocode 
        while high < len(nums):
            summ = summ + nums[high]   # adding and adding until reaching target
            while summ >= target:
                length = (high - low) + 1    # finding the length of the subarray which reached the target
                res = min(res, length)
                summ = summ - nums[low]     # now shrinking window
                low += 1
            high += 1                      # expanding window 
        if res == float("inf"):
            return 0                 # if res never updated likewise sum<target always 
        else:
            return res