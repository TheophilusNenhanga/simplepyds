from typing import Callable, Literal, Any
from simplepyds.Tree.TreeNode import BinarySearchTreeNode


class BinarySearchTree[T]:

    def __init__(self, comparator: Callable[[T, T], bool] | None = None):
        self._head: BinarySearchTreeNode[T] | None = None
        self._size: int = 0
        self._comparator = comparator
        self._type = None

    def check_type(self, value: T):
        if self._type is not None:
            if not isinstance(value, self._type):
                raise TypeError(f"'{value}' is not of type {self._type}")
        else:
            self._type = type(value)

    def insert(self, value: T):
        self.check_type(value)

        if self.is_empty():
            self._head = BinarySearchTreeNode(value)
            self._size += 1
            return

        self._head = self._insert(self._head, value)
        self._size += 1

    def _insert(self, root: "BinarySearchTreeNode[T] | None", value: T):
        if root is None:
            return BinarySearchTreeNode(value)

        if isinstance(value, (int, float, str)):
            if root is not None:
                if root.value >= value:
                    root.left = self._insert(root.left, value)
                if root.value < value:
                    root.right = self._insert(root.right, value)
        else:
            if self._comparator:
                if root is not None:
                    if self._comparator(root.value, value):
                        root.left = self._insert(root.left, value)
                    if self._comparator(value, root.value):
                        root.right = self._insert(root.right, value)
            else:
                raise NotImplementedError(f"Cannot compare <{type(self._type)}> without a comparator.\n"
                                          f"Please set a comparator.")

        return root

    def traverse(self, mode: Literal["in-order", "pre-order", "post-order"] = "in-order"):
        self._traverse(self._head, mode)

    def _traverse(self, root: BinarySearchTreeNode[T] | None, mode: Literal["in-order", "pre-order", "post-order"] = "in-order", visit: Callable[[T], Any] | None = None):
        if root is not None:
            if mode == "pre-order":
                if visit is not None:
                    visit(root.value)
                self._traverse(root.left, mode, visit)
                self._traverse(root.right, mode, visit)

            if mode == "in-order":
                self._traverse(root.left, mode, visit)
                if visit is not None:
                    visit(root.value)
                self._traverse(root.right, mode, visit)

            if mode == "post-order":
                self._traverse(root.left, mode, visit)
                self._traverse(root.right, mode, visit)
                if visit is not None:
                    visit(root.value)

    def head(self):
        if self._head is not None:
            return self._head.value

    def is_empty(self):
        return True if self._head is None else False

    def size(self):
        return self._size

    def foreach(self, visit_fn: Callable[[T], Any]):
        if not self.is_empty():
            self._traverse(self._head, mode="in-order", visit=visit_fn)

    def __str__(self):
        if self._head is not None:
            return (f"Head: {self._head}\n"
                    f"\tleft: {self._head.left}\n"
                    f"\tright: {self._head.right}")
        else:
            return str(None)
