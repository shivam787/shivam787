class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Binarysearchtree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else: 
            curr_node= self.root
            while True:
                if data< curr_node.data:
                    curr_node.left = new_node
                    return
                else:
                    curr_node = curr_node.left
        if data> curr_node.left:
            #right
                if curr_node.right= None:
                    curr_node= new_node
                    return
                else:
                    curr_node = curr_node.right
    def lookup(self, data):
        curr_node = =self.root
        while True:
            if curr_node = None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
    def print_tree(self):
        if self.root != None:
            self.print(self.root)
