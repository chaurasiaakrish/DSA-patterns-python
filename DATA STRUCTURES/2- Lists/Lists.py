# # list initialization
# l=[1,2,3,4,5,6]

# #len()
# print(len(l)) # prints the length of the list

# #negative indexing
# print(l[-1]) # negative indexing can also be done

# # append()
# a=-5
# l.append(a)
# print(l) # when appended the appended element will come at last

# # list append inside list
# l2=[7,8,9,10]
# l.append(l2)
# print(l) # a list wil be appended insisde a list at the last and will be considered as a single index
# print(l[7]) # [7,8,9,10] will be the output

# # extend()
# l3=[11,12,13,14,15]
# l.extend(l3)
# print(l) # list will be appended inside the list but piecewise elemnt wise at last
# # It helps in reducing the time complexity by removing loop to append

# # insert()
# l.insert(0,-7) #insert -7 at the index 0th 
# print(l) # all the elemnts will shift forward 
# # in append insertion takes place at last so to insert at specific position use #insert along with index number as a first argument 

# # remove() and pop() and clear()
# # remove specific element and pop removes from specific index
# l.remove(6)
# print(l) # element 6 will be removed
# l.pop(0)
# print(l) # index 0th element will be removed 
# l3.clear()
# print(l3) # whole l3 got cleared

# # min() and max()
# l4=[7,18,45]
# print(min(l4)) # o(n) time complexity
# print(max(l4)) # o(n) time complexity

# # count()
# l5=[1,1,1,2,3,4,5,5,6]
# print(l5.count(3))
# print(l5.count(1))
# print(l5.count(5))

# # sort() and sorted()
# l6=[7,45,18]
# l6.sort() # change in place and no extra space required and time complexity is o(nlogn)
# print("When used .sort",l6)
# l7=sorted(l6) # changes and saves in another list and original list will be as it is
# print("When used sorted",l7)

# reverse()
l8=[1,2,3]
l8.reverse() # o(n)
print(l8)