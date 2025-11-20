class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")

print("Root:", root.data)
print("Left child of root:", root.left.data)
print("Right child of root:", root.right.data)
print("Left child of B:", root.left.left.data)
