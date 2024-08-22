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

    def find(self, value) -> bool:
        """find
        :param value = hledaná hodnota
        :return true pokud je hodnota v binárním stromě
        """
        if self.value == value:
            return True
        if self.left and value < self.value:
            return self.left.find(value)
        elif self.right and value > self.value:
            return self.right.find(value)
        return False

    def deep(self):
        """
        Vrátí hloubku daného stromu
        :return: hloubka
        """
        left_deep = 0
        if self.left:
            left_deep = self.left.deep()
        right_deep = 0
        if self.right:
            right_deep = self.right.deep()
        return 1 + max(left_deep, right_deep)


    """ 
    Homework:
    Napište metody, které provedou průchod binárním stromem v 
    - preorder, 
    - inorder,
    - postorder a
    - level order pořadí a vrátí seznam.
    """

    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def level_order(self):
        pass

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

    for number in range(1, 20):
        print(f"{number} -> {binary_tree.find(number)}")

    binary_tree2 = BinaryTree(10)
    print(f"binary_tree has deep {binary_tree.deep()}")
    print(f"binary_tree2 has deep {binary_tree2.deep()}")

    numbers = range(1,20)
    binary_tree3 = BinaryTree(0)
    for number in numbers:
        binary_tree3.add(number)
    print(f"binary_tree3 has deep {binary_tree3.deep()}")

    print(f"binary_tree.inorder(): {binary_tree.inorder()}")
    print(f"binary_tree.preorder(): {binary_tree.preorder()}")
    print(f"binary_tree.postorder(): {binary_tree.postorder()}")
    print(f"binary_tree.level_order(): {binary_tree.level_order()}")
