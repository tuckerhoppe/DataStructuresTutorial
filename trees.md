# overview
Trees are like linked lists in that they are a bunch of items with pointers. A tree is made up of nodes pointing to parent nodes and child nodes. If it is the first node in the tree it won't point to a parent. And if it doesn't have any children it will only point to its parent node. A tree uses recursion to traverse the tree.


# Common Operations 
Trees are not built into Python. For this reason implementation of each of these operations might differ. Many of these operations use Recursion. Simply put recursion is when a function calls itself.
here is a link for more on recursion:https://byui-cse.github.io/cse212-course/lesson08/08-prepare.html

Inserting a value. This is done by recursively searching the subtrees and finding the next available spot. The perfomanceis O(log n)
```python
def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data == node.data:
                return
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```

Removing a value. Using recursion, search the subtrees to find the value to remove. This will require some adjusting and cleanup of the tree afterwards. The performance is O(log n)

Contains a value. To see if a value is in the search tree you have to recursively search the tree. The performance is O(log n)

Traverse forward. This operation recursively visits every piece of the tree. It's performance is O(n)

Traverse in reverse This operation also visits every part of the tree, but in reverse. The Performance is also O(n)

Height. This recursively finds the height of the tree by traversing the tree and keeping track of it.

Size. This is stored as an attribute of the Tree class. For this reason the performance is O(1)

Empty. This is also O(1). Take the root node and compare it to the size.

# advantages
A tree is a Hierarchy of storing data. This means all of the data will have a Relationship to eachother. So for any kind of data that is useful to know the relationship between the two, it is very useful!

# disadvantages
Small changes can cause large change in structure. Kind of unstable. You also have to write it by hand in python.

# Practice Problem
A company is having difficulties tracking who is doing what work and for what departments. When a poject is brought up by the ceo it is hard to track the department it was under and the Team that worked on it. See if what you have learned about binary search trees can help the company.(You can use a diagram or a python program)
CEO: Matt Jenkins
Departments:Marketing, HR, product design, product development
Team Leads: Tim(Marketing), Jill(HR), Michael(Product design), Mark(Product development), Toby(HR)
other Employees:
John: works in marketing. designed the "Sleek" Commercial
Harry: Works in marketing.
Joyce: works in product design. She lead on the new tire project
Tucker: Product development. Wrote the code for the new self driving car

```python
#STARTING CODE
from graphviz import Source
```

[Solution Code Link(https://github.com/tuckerhoppe/DataStructuresTutorial/blob/main/Treesolution.py)]



