# Python's heapq is a min heap by default. For numeric values, a common technique is to insert their negatives.
import heapq
nums = [5, 2, 8, 1, 9]
heap = []
for num in nums:    
    heapq.heappush(heap, -num)
print(-heapq.heappop(heap))  # 9
print(-heapq.heappop(heap))  # 8

# Why does this work?
# Original values:  5, 2, 8, 1, 9
# Negative values: -5,-2,-8,-1,-9