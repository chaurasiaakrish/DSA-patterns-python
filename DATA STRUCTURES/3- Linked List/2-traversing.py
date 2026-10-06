# Creating the linked list

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40) 

# Connecting each node to the next
node1.next=node2
node2.next=node3
node3.next=node4

# Initializing head of the linked list
head=node1

# Traversing the linked list
current_node=head
while current_node is not None:
    print(current_node.value)
    current_node=current_node.next