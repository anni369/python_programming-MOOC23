class Node:
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    max_value = root.value
    if root.left_child:
        if greatest_node(root.left_child) > max_value:
            max_value = greatest_node(root.left_child)
    if root.right_child:
        if greatest_node(root.right_child) > max_value:
            max_value = greatest_node(root.right_child)
    return max_value

if __name__ == "__main__":
    
    tree = Node(2)
    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
    print(greatest_node(tree))