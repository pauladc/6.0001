# Problem Set 4a
# Name: Paula Contreras
# Collaborators: None
# Time spent: 3:00
# Late days: 1

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(5)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(4), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(19), Node(26)))) #TODO

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # check that node exists and find max between height of both branches
    # adds one through each iteration
    if tree != None:
        return max(find_tree_height(tree.get_left_child()), find_tree_height(tree.get_right_child())) + 1
    else:
        return -1



def is_heap(tree,compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # a leaf is always a heap
    if tree.get_right_child() == None:
        right_side = True
    if tree.get_left_child() == None:
        left_side = True
        
    if tree.get_left_child() == None and tree.get_right_child() == None:
            return True
    # checks to see if right branch exists
    if tree.get_right_child() != None:
        # calls recursion if true
        if compare_func(tree.get_right_child().get_value(), tree.get_value()) == True:
            right_side = is_heap(tree.get_right_child(), compare_func)
        # returns false and breaks recursion if wrong val found
        else:
            return False
    # checks to see if left branch exists
    if tree.get_left_child() != None:
        # calls recursion if true
        if compare_func(tree.get_left_child().get_value(), tree.get_value()) == True:
            left_side = is_heap(tree.get_left_child(), compare_func)
        # returns false and breaks recursion if wrong val found
        else:
            return False
    if left_side and right_side:
        return True



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
