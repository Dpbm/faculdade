class Node:
    def __init__(self, data):
        self.data = data
        self.children = [ ]
    
    def add_child(self,child):
        self.children.append(Node(child))
        return self.children[-1]

tree = Node(1)

first  = tree.add_child(2)
second = tree.add_child(3)
third  = tree.add_child(4)

fifth = first.add_child(5)

print_tree(tree)
