class AVLTReeNode(object):
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

        self.count = 1

    #returns the new root
    def insert(self, node):
        if node.key <= self.key:
            if self.left is None:
                self.left = node
            else:
                self.left = self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right = self.right.insert(node)

        update_height(self)
        self.count += 1
        return self._balance()

    # Performs rotations to create an AVL tree and returns the new root.
    # Assumes all children are balanced (have AVL property).
    def _balance(self):
        new_root = self
        
        #now rotate...
        left_height = get_height(self.left)
        right_height = get_height(self.right)

        if left_height + 2 <= right_height:
            if get_height(self.right.left) > get_height(self.right.right):
                self.right = rotate_right(self.right)

            new_root = rotate_left(self)

        elif left_height >= right_height + 2:
            #symmetric situtation... swap left with right somehow
            if get_height(self.left.right) > get_height(self.left.left):
                self.left = rotate_left(self.left)

            new_root = rotate_right(self)

        return new_root


    #the "delete by copy" technique. Returns the new root
    def delete_root(self):
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left

        #now get rightmost of the left
        curr_node = self.left
        if curr_node.right is None:
            curr_node.right = self.right
            update_count(curr_node)
            return curr_node._balance()

        visited_nodes = []
        while curr_node.right is not None:
            visited_nodes.append(curr_node)
            curr_node = curr_node.right

        self.key = curr_node.key
        child = curr_node.left

        while len(visited_nodes) > 0:
            node = visited_nodes.pop()
            node.right = child
            update_count(node)
            child = node._balance()

        self.left = child
        update_count(self)
        return self._balance()

    def delete(self, key):
        if self.key == key:
            return self.delete_root()
        elif key < self.key:
            if self.left is None:
                raise Exception("Key {key} not found".format(key = key))
            self.left = self.left.delete(key)
        elif self.key < key:
            if self.right is None:
                raise Exception("Key {key} not found".format(key = key))
            self.right = self.right.delete(key)

        self.count -= 1
        return self._balance()
        
    def to_sorted_array(self):
        array = []
        if self.left is not None:
            array.extend(self.left.to_sorted_array())

        array.append(self.key)

        if self.right is not None:
            array.extend(self.right.to_sorted_array())

        return array

    def count_less(self, upper):
        result = 0
        if self.key < upper:
            result += 1
            result += get_count(self.left)
            if self.right is not None:
                result += self.right.count_less(upper)
        else:
            if self.left is not None:
                result += self.left.count_less(upper)

        return result 


def get_height(node):
    if node is None:
        return 0
    return node.height

def get_count(node):
    if node is None:
        return 0
    return node.count

#assumes all children have had their heights updated
def update_height(tree_node):
    if tree_node is None:
        return
    tree_node.height = max(get_height(tree_node.right) + 1, get_height(tree_node.left) + 1)

#assumes all children have had their counts updated
def update_count(tree_node):
    if tree_node is None:
        return
    tree_node.count = 1 + get_count(tree_node.left) + get_count(tree_node.right)

def rotate_left(root):
    new_root = root.right
    root_right_left = root.right.left
    new_root.left = root
    new_root.left.right = root_right_left

    update_height(new_root.left)
    update_height(new_root)
    update_count(new_root.left)
    update_count(new_root)

    return new_root

def rotate_right(root):
    new_root = root.left
    root_left_right = root.left.right
    new_root.right = root
    new_root.right.left = root_left_right

    update_height(new_root.right)
    update_height(new_root)
    update_count(new_root.right)
    update_count(new_root)

    return new_root