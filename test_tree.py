from tree import Tree
import unittest

class TestTree(unittest.TestCase):

    def setUp(self):
        self.test_tree = Tree()

        for i in range (1, 7):
            self.test_tree.add(i)

    def test_find1(self):
        assert self.test_tree._find(2, self.test_tree.root) is not None

    def test_find2(self):
        assert self.test_tree._find(10, self.test_tree.root) is None

if __name__ == "__main__":
    unittest.main()