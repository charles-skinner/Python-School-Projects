"""
binary search tree class
"""


class Node:
    """
    class for nodes
    """
    def __init__(self,pair):
        self.pair = pair
        self.left = None
        self.right = None
        self.parent = None
    

class BST:
    """
    class for the binary search tree
    """
    def __init__(self):
        """
        initializer
        """
        self.root = None
        self.lyst = []


    def is_empty(self):
        """
        docstring
        """
        if self.root:
            return False
        return True


    def size(self):
        """
        Return the number of items in the tree.
        """
        return len(self.inorder())


    def height(self):
        """
        Return the height of the tree, which is the length 
        of the path from the root to its deepest leaf.     
        """
        return(self.height_recurser(self.root))
        

    def height_recurser(self,node):
        """
        does the recursion for height()
        """
        if node is None:
            return 0
        leftHeight = self.height_recurser(node.left)
        rightHeight = self.height_recurser(node.right)
        return 1 + max(leftHeight,rightHeight)


    def add(self,item):
        """
        Add item to its proper place in the tree. Return the modified tree. 
        """
        new = Node(item)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while current is not None:
                if new.pair.letter < current.pair.letter:
                    if current.left is None:
                        current.left = new
                        current = None
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new
                        current = None
                    else:
                        current = current.right                    
        return self


    def remove(self,item):
        """
        Remove item from the tree. Return the modified tree.
        """
        parent = None
        current = self.root
        while current is not None:
            if current.pair.letter == item.letter:
                if (current.left is None) and (current.right is None):
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                else:
                    successor = current.right
                    while successor.left is not None:
                        successor = successor.left
                    successor_pair = successor.pair
                    self.remove(successor_pair)
                    current.pair = successor_pair
                return None
            elif current.pair.letter < item.letter:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        return None

    
    def find(self,item):
        """
        Return the matched item. If item is not in the tree, raise a ValueError.
        """
        current = self.root
        while current is not None:
            if item.letter == current.pair.letter:
                return current.pair
            elif item.letter < current.pair.letter:
                current = current.left
            else:
                current = current.right
        raise ValueError


    def inorder(self):
        """
         Return a lyst with the data items in order of inorder traversal.
        """
        self.lyst = []
        self.inorder_recurser(self.root)
        return self.lyst
    

    def inorder_recurser(self,node):
        """
        does recursion for inorder
        """
        if node is None:
            return
        self.inorder_recurser(node.left)
        self.lyst.append(node.pair)
        self.inorder_recurser(node.right)
        

    def preorder(self):
        """
        Return a list with the data items in order of preorder traversal.
        """
        self.lyst = []
        self.preorder_recurser(self.root)
        return self.lyst


    def preorder_recurser(self,node):
        """
        does recursion for preorder
        """
        if node is None:
            return
        self.lyst.append(node.pair)
        self.preorder_recurser(node.left)
        self.preorder_recurser(node.right)


    def postorder(self):
        """
        Return a list with the data items in order of postorder traversal.
        """
        self.lyst = []
        self.postorder_recurser(self.root)
        return self.lyst


    def postorder_recurser(self,node):
        """
        does recursion for postorder
        """
        if node is None:
            return
        self.postorder_recurser(node.left)
        self.postorder_recurser(node.right)
        self.lyst.append(node.pair)


    def rebalance(self):
        """
        rebalance the tree. Return the modified tree.
        """
        lyst = self.inorder()
        self.root = None
        self.rebalance_recurser(lyst)
        return self
    

    def rebalance_recurser(self,lyst):
        """
        docstring
        """
        if lyst == []:
            return
        mid = len(lyst)//2
        self.add(lyst[mid])
        self.rebalance_recurser(lyst[0:mid])
        self.rebalance_recurser(lyst[mid+1:len(lyst)])