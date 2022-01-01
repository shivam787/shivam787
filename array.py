class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data
class Linkedlist:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            nodes = node.next
        node.append("None")
        return " -> ".join(nodes)
llist = Linkedlist()
first_node = Node('a')
llist.head = first_node
second_node = Node ('b')
third_node = Node ('c')
fourth_node = Node ('d')
first_node.next = second_node
second_node.next = third_node
second_node.next = fourth_node
