# Python's built-in heapq provides a min heap.

import heapq     # a way to import heapq built in function present in python to implement heap

# A. insertion or construction of the heap

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
print(heap[0])  # 1
# by default min heap = [1, 2, 8, 5]
# Don't expect it to be fully sorted. It only needs to satisfy the heap property.


# B. Remove the minimum element
smallest = heapq.heappop(heap)
print(smallest)  # 1
# heappop() removes and returns the smallest element.
# If you repeatedly pop, the values come out in ascending order.


# C. Convert an existing list into a heap
nums = [7, 2, 9, 1, 5]
heapq.heapify(nums)
print(nums[0])  # 1
# heapify() transforms the list into a valid min heap in place.