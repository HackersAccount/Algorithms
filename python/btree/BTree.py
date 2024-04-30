# Tree
from BTreeNode import BTreeNode


class BTree:
    def __init__(self, t):
        """
        Initializes a B-tree.

        Args:
        - t (int): Minimum degree of the B-tree.
        """
        self.root = BTreeNode(True)  # Create a root node with leaf set to True
        self.t = t

    # Insert node
    def insert(self, k):
        """
        Inserts a key into the B-tree.

        Args:
        - k (tuple): Key to be inserted as a tuple (key, value).
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    # Insert nonfull
    def insert_non_full(self, x, k):
        """
        Inserts a key into a non-full node in the B-tree.

        Args:
        - x (BTreeNode): Node in which the key is to be inserted.
        - k (tuple): Key to be inserted as a tuple (key, value).
        """
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Split the child
    def split_child(self, x, i):
        """
        Splits a child node of a B-tree node.

        Args:
        - x (BTreeNode): Parent node.
        - i (int): Index of the child node to be split.
        """
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]
        if not y.leaf:
            z.child = y.child[t : 2 * t]
            y.child = y.child[0 : t - 1]

    # Print the tree
    def print_tree(self, x, l=0):
        """
        Prints the B-tree.

        Args:
        - x (BTreeNode): Node to be printed.
        - l (int): Level of the node in the tree (default: 0).
        """
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    # Search key in the tree
    def search_key(self, k, x=None):
        """
        Searches for a key in the B-tree.

        Args:
        - k (int): Key to search for.
        - x (BTreeNode): Node to start the search from (default: None).

        Returns:
        - tuple: A tuple containing the node and index of the key if found, None otherwise.
        """
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)