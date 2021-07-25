class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

# Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


head_list = doubly_linked_list()
head_list.push(12)
head_list.push(8)
head_list.push(62)
head_list.listprint(head_list.head)
