from BTree import BTree


def main():
    B = BTree(3)  # Create a B-tree with minimum degree 3

    # Insert keys into the B-tree
    for i in range(10):
        B.insert((i, 2 * i))

    # Print the B-tree
    B.print_tree(B.root)

    # Search for a key in the B-tree
    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == "__main__":
    main()
