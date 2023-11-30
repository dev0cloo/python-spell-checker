# Import =====================================================================================
from python_spell.src.binarytree import Node as inheritance
# ============================================================================================


class Item(inheritance):
    """
    An item for linked lists\n
    Note that it is only for linked lists. In the case of hash tables, please use the 'Node' class
    """

    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer

    def getNextNode(self):
        return self.pointer

    def __str__(self):

        return str(self.val)

    def get_children(self):
        """
        Invalid Method!
        """
        pass

    def print_tree(self, val="val", left="left", right="right"):
        """
        Invalid Method!
        """
        pass

    def display(self):
        """
        Display the linked list using arrows
        """
        buffer = "Linked list: \n"
        node = self
        while node.pointer != None:
            buffer += f"{node.val} -> "
            node = node.pointer
        buffer += f"{node.val}"
        print(buffer)

    def appendChild(self, *args):
        """
        Append child to the linked list or the item(whatever you like to call it)
        """
        for child in args:
            tmp = self
            if self.pointer == None:
                self.pointer = child
                while tmp.pointer != None:
                    tmp = tmp.pointer
            else:
                while tmp.pointer != None:
                    tmp = tmp.pointer
                tmp.pointer = child
