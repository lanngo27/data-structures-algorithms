'''
Created on 28.11.2017

@author: Artturi Tilanterä
'''

from collections import deque
from bst import BSTNode, BST

def print_bst(bst):
    """Prints the given binary search tree."""
    text_tree = TextTree()
    text_tree.build_from_BST(bst)
    print(text_tree.get_visualisation())

class TextNode:
    """Represents a binary search tree node prepared for a text-based
    visualisation."""
    def __init__(self, key, ypos):
        self.key = key          # Integer in range [0,99]
        self.ypos = 0           # Characters from top
        self.xpos = 0           # Characters from left
        self.left = None        # Left child
        self.right = None       # Right child
        self.left_width = 0     # Width of left subtree
        self.right_width = 0    # Width of right subtree
        self.width = 2          # Width of this node + subtrees

class TextTree:
    """Creates UTF-8 encoded text visualisations of binary search trees.
    Example:
                  50
           ┌───────┴───────┐
          25              75
       ┌───┴───┐       ┌───┴───┐
      12      40      60      80
     ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    06  24  30  42  53  65  79  93"""
     
    def __init__(self):
        self.root = None
        
    def build_from_BST(self, bst):
        """Builds the text tree from a binary search tree."""
        if (bst == None or bst.root == None):
            self.root = None
            return
        self.root = TextNode(bst.root.key, 0)
        self._visited_nodes = set()        
        self._visit_BST_postorder(bst.root, self.root, 0)
        self._compute_xpos(self.root, 0)
       
        
    def _visit_BST_postorder(self, bst_node, text_node, ypos):
        """Recursively visits a BST in postorder and builds a tree of
        TextNodes."""
        if (bst_node in self._visited_nodes):
            raise KeyError("Node with key {} was seen repeatedly! This is "
            "not a binary tree.".format(bst_node.key))
        
        if (bst_node.left != None):
            text_node.left = TextNode(bst_node.left.key, ypos + 1)
            self._visit_BST_postorder(bst_node.left, text_node.left, ypos + 1)
            text_node.left_width = text_node.left.width

        if (bst_node.right != None):
            text_node.right = TextNode(bst_node.right.key, ypos + 1)
            self._visit_BST_postorder(bst_node.right, text_node.right, ypos + 1)
            text_node.right_width = text_node.right.width
        
        text_node.width = text_node.left_width + 2 + text_node.right_width
        text_node.ypos = ypos
        self._visited_nodes.add(bst_node)    
    
    def _compute_xpos(self, node, starting_xpos):
        """Computes x positions for the nodes."""
        if (node is None):
            return starting_xpos
        node.xpos = self._compute_xpos(node.left, starting_xpos)
        return self._compute_xpos(node.right, node.xpos + 2)
                
    def print_levelorder(self):
        """Test method: prints nodes of the tree in level order with x and y
        positions."""
        if (self.root == None):            
            return "(empty tree)"
        q = deque()
        q.appendleft(self.root)
        output = ""
        while (len(q) > 0):
            node = q.pop()
            output += "Key: {} ypos: {} xpos: {}\n".format(node.key, node.ypos,
                node.xpos)
            if (node.left != None):
                q.appendleft(node.left)
            if (node.right != None):
                q.appendleft(node.right)
        return output
        
    def get_visualisation(self):
        """Returns a multiline string containing the final visualisation of
        the tree."""
        if (self.root == None):            
            return "(empty tree)"
        q = deque()
        q.appendleft(self.root)
        output = ""
        nodes_on_level = []     # Nodes on current level
        cursor_ypos = -1
        cursor_xpos = 0
        
        # Iterate nodes in level order
        while (len(q) > 0):
            node = q.pop()
            
            if (node.ypos > cursor_ypos):
                # New level in the tree. Print edges from previous level.
                output += self._print_edge_line(nodes_on_level)
                nodes_on_level = []
                cursor_xpos = 0
                cursor_ypos += 1
                
            
            if (cursor_xpos < node.xpos):
                # Padding from left
                output += " " * (node.xpos - cursor_xpos)
            cursor_xpos = node.xpos
            
            # Node text (2 characters)
            output += "{0:2}".format(node.key)
            cursor_xpos += 2
            nodes_on_level.append(node)
            
            # For level order iteration
            if (node.left != None):
                q.appendleft(node.left)
            if (node.right != None):
                q.appendleft(node.right)

        output += "\n"
        return output
    
    def _print_edge_line(self, node_list):
        """Helper function for get_visualisation. Prints edges from nodes in
        given node_list to their children. Returns a single-line string.""" 
        if (len(node_list) == 0):
            return ""

        #    20
        #   ┌─┴─────────┐    <- draw this line
        #   2          64
        #
        #
        output = "\n"
        cursor_xpos = 0
        for node in node_list:
            if (node.left != None):
                next_x = node.left.xpos + 1
                output += " " * (next_x - cursor_xpos)  # left padding
                output += "┌"                           # hook to left child
                cursor_xpos = node.left.xpos + 2
                next_x = node.xpos + 1
                output += "─" * (next_x - cursor_xpos)  # horizontal line to
                                                        # current node
                # hook at current node
                if (node.right != None):                
                    output += "┴"
                else:                
                    output += "┘"
                cursor_xpos = node.xpos + 2
                
            if (node.right != None):
                if (node.left == None):
                    next_x = node.xpos + 1
                    output += " " * (next_x - cursor_xpos) # left padding
                    output += "└"                          # hook at current
                    cursor_xpos = next_x + 1
                
                next_x = node.right.xpos + 1
                output += "─" * (next_x - cursor_xpos) # horizontal line to
                                                       # current node
                output += "┐"                          # hook to right child
                cursor_xpos = node.right.xpos + 2
        output += "\n"
        return output    
