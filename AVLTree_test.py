import unittest

from AVLTree import *

def test_AVL_property(node):
    if node is None:
        return True
    if abs(calc_tree_height(node.left) - calc_tree_height(node.right)) > 1:
        return False
    if test_AVL_property(node.left) == False:
        return False
    if test_AVL_property(node.right) == False:
        return False

    return True

class TestAVLTree(unittest.TestCase):
    def test_insert(self, node_keys_arr = [0,1,2,3,4,5]):
        tree = AVLTree()
        for key in node_keys_arr:
            tree.insert_key(key)
            self.assertTrue(test_AVL_property(tree.root))

        self.assertEqual(tree.to_sorted_array(), sorted(node_keys_arr))
        self.assertEqual(calc_tree_height(tree.root), tree.root.height)

    def test_delete(self, node_keys_arr = [0,1,2,3,4,5]):
        tree = AVLTree()
        for key in node_keys_arr:
            tree.insert_key(key)

        for i in range(1,len(node_keys_arr)):
            self.assertTrue(test_AVL_property(tree.root))
            tree.delete(node_keys_arr[-i])
            self.assertEqual(tree.to_sorted_array(), sorted(node_keys_arr[:-i]))


    def test_count(self, node_keys_arr = [0,1,2,3,4,5]):
        tree = AVLTree()
        for key in node_keys_arr:
            tree.insert_key(key)

        self.assertEqual(tree.root.count, len(node_keys_arr))
        nodes_to_visit = [tree.root]
        while nodes_to_visit:
            next_nodes_to_visit = []
            for node in nodes_to_visit:
                self.assertEqual(node.count, count_elements_tree(node))
                if node.left is not None:
                    next_nodes_to_visit.append(node.left)
                if node.right is not None:
                    next_nodes_to_visit.append(node.right)
            nodes_to_visit = next_nodes_to_visit

    def test_count_less(self, node_keys_arr = [0,1,2,3,4,5]):
        tree = AVLTree()
        for key in node_keys_arr:
            tree.insert_key(key)
        
        keys_sorted = sorted(set(node_keys_arr))

        for i in range(len(keys_sorted)):
            self.assertEqual(tree.count_less(keys_sorted[i]), i)

def calc_tree_height(node):
    if node is None:
        return 0

    height = 1
    if node.left is not None:
        height = max(height, calc_tree_height(node.left) + 1) 
    if node.right is not None:
        height = max(height, calc_tree_height(node.right) + 1)

    return height

def count_elements_tree(tree_node):
    if tree_node is None:
        return 0

    count = 1
    count += count_elements_tree(tree_node.left)
    count += count_elements_tree(tree_node.right)
    return count

def plot_node(node):
    if node is None:
        return ""

    return "(" + plot_node(node.left) + " " + str(node.key) + " " + plot_node(node.right) + ")"

if __name__ == '__main__':
    unittest.main()