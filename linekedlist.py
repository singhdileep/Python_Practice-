# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# def detectLoop(head):
#     # Using set for hashtable.
#     hashtable = set()
#     ptr = head
#     while ptr != None:
#         # Check if node address already present.
#         if ptr in hashtable:
#             return True
#         # Add the current node address to hashtable.
#         hashtable.add(ptr)
#         ptr = ptr.next
#     return False


# if __name__ == "__main__":
#     head = ListNode(2)
#     head.next = l1 = ListNode(8)
#     l1.next = l2 = ListNode(3)
#     l2.next = l3 = ListNode(5)
#     l3.next = l4 = ListNode(10)
#     l4.next = None
#     # 2->8->3->5->10--
#     #   	^    	|
#     #   	|    	|
#     #   	---------
# print(detectLoop(head))





# class Node:
#     def __init__(self,data):
#         self.data=data
# def detectLoop(head):
#     l=[]
#     temp=head
#     while temp!=None:
#         if temp in l:
#             return True
#         l.append(temp)
#         temp=temp.next
#     return False 

# if __name__ == "__main__":
#     head = Node(2)
#     head.next = l1 = Node(8)
#     l1.next = l2 = Node(3)
#     l2.next = l3 = Node(5)
#     l3.next = l4 = Node(10)
#     l4.next = l1
# print(detectLoop(head))




# class Node():
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# class LinkedList():
#   def __init__(self, data):
#     a = Node(data)
#     self.head = a
    
# def insert_at_beginning(l, n):
#   n.next = l.head
#   l.head = n

# if __name__ == '__main__':
#   l = LinkedList(10)
# a = Node(20)
# b = Node(50)
# c = Node(60)

# l.head.next = a
# a.next = b
# b.next = c

# z = Node(0)
# insert_at_beginning(l, z)
# z = Node(-10)
# print(insert_at_beginning(l, z))  







