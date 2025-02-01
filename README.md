# avl_tree_py

Implements an [AVL tree](https://en.wikipedia.org/wiki/AVL_tree) in python. The advantage of this data structure is that insertion, deletion and counting how many elements are less than x are all O(log(n)) thus efficient. Note that for a hash map insertion and deletion is O(1) but counting how many elements are less than x is much slower, i.e., O(n).

|                 | Sorted Array | Hash-map | AVL tree |
|-----------------|--------------|----------|----------|
|Insert           |O(n)          | O(1)     | O(log(n))|
|Delete           |O(n)          | O(1)     | O(log(n))|
|Count less than x|O(log(n))     | O(n)     | O(log(n))|

Here is an example that is quite self-explanatory:

```
>>> from AVLTree import AVLTree
>>> tree = AVLTree()
>>> tree.insert_key(1)
>>> tree.insert_key(2)
>>> tree.insert_key(20)
>>> tree.insert_key(5)
>>> tree.insert_key(10)
>>> tree.to_sorted_array()
[1, 2, 5, 10, 20]
>>> tree.count_less(6)
3
>>> tree.count_less(4)
2
>>> tree.count_less(20)
4
>>> tree.count_less(20.5)
5
>>> tree.delete(5)
>>> tree.to_sorted_array()
[1, 2, 10, 20]
>>> tree.count_less(11)
3
```

To clarify, `tree.count_less(6)` gives `3` above because there are three numbers (`1`,`2` and `5`) that are less than `3`. This method has complexity O(log(n)).
