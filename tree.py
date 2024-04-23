from node import Node

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        
        """
            The method searches for a certain element recursively wothin the tree.
        """
        if data == node.data:
            return node
        elif (data != node.data and node.left is None and node.right is None):
            return None
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """
            The method deallocates the whole tree.
        """
        # TODO 1
        self.root = None

    def printTree(self):
        """
            The method prints all elements found within the tree inorder (left, root, right).
        """
        # TODO 1
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """
            The method does the inorder traversal of the tree.
        """
        # TODO 1
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """
            The method does the preorder traversal of the tree.
        """
        # TODO 2
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """
            The method does the postorder traversal of the tree.
        """
        # TODO 2
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')


