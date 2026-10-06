class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next # cycle detection PHASE 1
            if fast==slow:
                slow=head
                while fast!=slow:
                    slow=slow.next # node where cycle starts
                    fast=fast.next 
                return slow
        return None   
    
    
##  Floyd's Cycle for array 
    
nums=[1,2,2,3,4,5]
slow=0
fast=0
while fast< len(nums):
    slow=nums[slow]
    fast=nums[nums[fast]]
    if fast==slow:
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        print(slow)     