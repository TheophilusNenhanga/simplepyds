class BinarySearchTreeNode[T]:

    def __init__(self, value: T, left: "BinarySearchTreeNode[T] | None" = None, right: "BinarySearchTreeNode[T] | None" = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)
