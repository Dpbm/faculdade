class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, new_node, node):
        if(not node):
            return

        if(new_node.value == node.value):
            return

        if(new_node.value < node.value):
            
            if(not node.left):
                node.left = new_node
                return

            self.insert(new_node, node.left)
            return
            

        if(not node.right):
            node.right = new_node
            return

        self.insert(new_node, node.right)
    
    def search(self, value, node):
        if(not node):
            return

        if(value == node.value):
            return node

        if(value < node.value):
            return self.search(value, node.left)

        return self.search(value, node.right)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = Tree(Node(1))

tree.insert(Node(1), tree.root)
tree.insert(Node(2), tree.root)
tree.insert(Node(3), tree.root)

print(tree.root.value)
print(tree.root.right.value, end='\n\n')

found_item = tree.search(3, tree.root)

print(found_item.value)