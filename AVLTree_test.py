from AVLTree import *

def test_AVL_property(node):
    assert(abs(calc_tree_height(node.left) - calc_tree_height(node.right)) < 2)
    if node.left is not None:
        test_AVL_property(node.left)
    if node.right is not None:
        test_AVL_property(node.right)

def test_insert(node_keys_arr):
    tree = AVLTree()
    for key in node_keys_arr:
        tree.insert_key(key)
        test_AVL_property(tree.root)

    assert(tree.to_sorted_array() == sorted(node_keys_arr))
    print(plot_node(tree.root))
    assert(calc_tree_height(tree.root) == tree.root.height)

def test_delete(node_keys_arr = [0,1,2,3,4,5]):
    tree = AVLTree()
    for key in node_keys_arr:
        tree.insert_key(key)

    print(plot_node(tree.root))
    for i in range(1,len(node_keys_arr)):
        test_AVL_property(tree.root)
        tree.delete(node_keys_arr[-i])
        print(plot_node(tree.root))
        assert(tree.to_sorted_array() == sorted(node_keys_arr[:-i]))

def count_elements_tree(tree_node):
    if tree_node is None:
        return 0

    count = 1
    count += count_elements_tree(tree_node.left)
    count += count_elements_tree(tree_node.right)
    return count

def test_count(node_keys_arr = [0,1,2,3,4,5]):
    tree = AVLTree()
    for key in node_keys_arr:
        tree.insert_key(key)

    assert(tree.root.count == len(node_keys_arr))
    nodes_to_visit = [tree.root]
    while nodes_to_visit:
        next_nodes_to_visit = []
        for node in nodes_to_visit:
            assert(node.count == count_elements_tree(node))
            print(node.count)
            if node.left is not None:
                next_nodes_to_visit.append(node.left)
            if node.right is not None:
                next_nodes_to_visit.append(node.right)
        nodes_to_visit = next_nodes_to_visit

def calc_tree_height(node):
    if node is None:
        return 0

    height = 1
    if node.left is not None:
        height = max(height, calc_tree_height(node.left) + 1) 
    if node.right is not None:
        height = max(height, calc_tree_height(node.right) + 1)

    return height

def plot_node(node):
    if node is None:
        return ""

    return "(" + plot_node(node.left) + " " + str(node.key) + " " + plot_node(node.right) + ")"