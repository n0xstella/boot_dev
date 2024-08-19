#BigO Complexity of O(log(n))
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    #Tree traversal - Going down the tree
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited
    ##ALT
    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            visited.extend(self.left.preorder(self))
        if self.right:
            visited.extend(self.right.preorder(self))
        return visited
    
    #Tree Traversal - Going up the tree
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited
    
   #Tree Traversal -  Going in order
    def inorder(self, visited):
        if self.left is not None:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited
    
    #Check if given value exists in tree
    def exists(self, val):
        if self.val is None:
            return False
        if self.val == val:
            return True
        if val < self.val and self.left is not None:
            return self.left.exists(val)
        if val > self.val and self.right is not None:
            return self.right.exists(val)
        return False    

    def insert(self, val):
        if self.val is None:
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def _get_min_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def delete(self, val):
        if self.val is None:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else: 
            if self.left is None and self.right is None:  # No children
                return None
            if self.left is None:  # One child (right)
                return self.right
            if self.right is None:  # One child (left)
                return self.left

            # Two children
            min_larger_node = self.right._get_min_node()
            self.val = min_larger_node.val
            self.right = self.right.delete(min_larger_node.val)
                    
        return self

    def __repr__(self):
        return f"({self.val}, {self.left}, {self.right})"
    



    def search_range(self, lower_bound, upper_bound):
        visited = []
        if self.val is not None:
            visited.append(self.val)        
        if self.left is not None:
            visited.extend(self.left.search_range(lower_bound, upper_bound))
        if self.right is not None:
            visited.extend(self.right.search_range(lower_bound, upper_bound))
        return visited