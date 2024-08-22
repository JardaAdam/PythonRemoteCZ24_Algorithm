class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryTree(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryTree(value)

    def __str__(self):
        result = str(self.value) + ', '
        result += str(self.left) + ', '
        result += str(self.right) + ', '
        return result


if __name__ == '__main__':
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(7)
    root.left.left.left = BinaryTree(1)
    root.left.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(8)
    root.right = BinaryTree(12)
    root.right.left = BinaryTree(11)
    root.right.right = BinaryTree(15)

    binary_tree = BinaryTree(10)
    numbers = [10, 5, 3, 12, 11, 7, 15, 4, 8, 1]
    for number in numbers:
        binary_tree.add(number)
    print(binary_tree)
