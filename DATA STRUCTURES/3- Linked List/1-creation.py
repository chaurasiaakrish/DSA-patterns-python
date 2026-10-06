class Node:
    def __init__(self, value):   # runs when object is created
        self.value = value      # stores data
        self.next = None        # link to next node

node1 = Node(10)                 # create first node
print(node1.value)               # print value of first node
print(node1.next)                # print next of first node (None)

# node1
#   ↓
# ┌───────┬───────┐
# │  10   │ None  │
# └───────┴───────┘

node1=Node(20)                 # create second node
node2 = Node(30)                 # create third node
node3 = Node(40)                 # create fourth node

# node1       node2       node3
#   ↓           ↓           ↓
# 10 → None   20 → None   30 → None

# Connecting each node to the next

node1.next=node2
node2.next=node3

# node1
#   ↓
# 10 → 20 → 30 → None

head=node1

# head
#   ↓
# 10 → 20 → 30 → None