# when the sixe of the window is fixed
class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low =0
        high=low+(k-1)
        summ=0
        maxi=0
        for i in range(low,high+1):  # in sliding window first iteration is different from all that's it
            summ=summ+arr[i]
        maxi=summ  # remember for negative sum, max=max(maxi,summ) will cause problem
        low+=1
        high=low+(k-1)
        while(high<len(arr)):  # same 2 ointer type 
            summ=summ+arr[high]-arr[low-1]  # no need to claculate much summ + incoming - outgoing
            maxi=max(summ,maxi) # then updating that maxi wrt summ
            low+=1
            high+=1
        return maxi    # returning the largest summm.
            