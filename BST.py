# Binary Search Tree implementation in python

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
            
    def insert_helper(self, current, new_val):
        if new_val < current.value:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        else:
            if current.right:
                self.insert_helper(current.left, new_val)
            else:
                current.right = Node(new_val)
    
    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current.value == find_val:
            return True
        elif find_val < current.value:
            if current.left:
                return self.search_helper(current.left, find_val)
        else:
            if current.right:
                return self.search_helper(current.right, find_val)
        return False
    