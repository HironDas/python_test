class Node:
    '''Class representing one node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''Class representing a linked list data structur'''
    def __init__(self, head):
        self.head = head
    def add(self, head):
        '''Add a new node to the linked list'''
        previous_head = self.head
        self.head = Node(data)
        self.head.next = previous_head
