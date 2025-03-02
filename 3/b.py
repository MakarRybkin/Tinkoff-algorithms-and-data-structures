from sys import stdin

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)

def abs_value(x):
    return -x if x < 0 else x

def is_avl_util(node, min_value, max_value):
    if node is None:
        return True

    if node.value <= min_value or node.value >= max_value:
        return False

    left_height = height(node.left)
    right_height = height(node.right)

    if abs_value(left_height - right_height) > 1:
        return False

    return (is_avl_util(node.left, min_value, node.value) and
            is_avl_util(node.right, node.value, max_value))

def is_avl_tree(root):
    return is_avl_util(root, float('-inf'), float('inf'))

# Чтение входных данных
n, root_index = [int(x) for x in stdin.readline().split()]

tree = [Node(i) for i in range(n)]

for i in range(n):
    num1, num2 = [int(x) for x in stdin.readline().split()]
    if num1 != -1:
        tree[i].left = tree[num1]
    if num2 != -1:
        tree[i].right = tree[num2]

# Проверка, является ли дерево AVL-деревом
if is_avl_tree(tree[root_index]):
    print(1)
else:
    print(0)
