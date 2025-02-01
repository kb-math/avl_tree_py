from AVLTreeNode import *

class AVLTree(object):
    def __init__(self, root = None):
        self.root = root

    def insert_node(self, node):
        if self.root is None:
            self.root = node
            return

        self.root = self.root.insert(node)

    def delete_root(self):
        self.root = self.root.delete_root()

    def delete(self, key):
        new_root = self.root
        try:
            new_root = self.root.delete(key)
        except Exception as err:
            print(err)
        self.root = new_root
    def to_sorted_array(self):
        return self.root.to_sorted_array()

    def insert_key(self, key):
        self.insert_node(AVLTReeNode(key))

    def count_less(self, upper):
        if self.root is None:
            return 0

        return self.root.count_less(upper)
