# Import
# ========================================================================
from python_spell.src.linkedlist import Item
# ========================================================================

# Classes
# ========================================================================


class Node(Item):
    """
    A node for hash tables
    """

    def appendChild(self, *args):
        return None
# ========================================================================


class Hashtable:
    """
    A data structure that organizes your data more efficiently\n
    Has only one property(or attribute, or field, or whatever you like, ok?)
    """
    SIZE = 456976
    tracking_list = []

    def __init__(self):
        """
        Initializes the linked list
        """
        self.nodes = [None] * self.SIZE

    def hash(self, string):
        """
        Returns the hash value of a node.
        """
        hashFV = 0
        string = str(string)
        for char in string:
            hashFV += ord(char.lower())

        return hashFV % self.SIZE

    def insert(self, *nodes: Node):
        """
        Adding an node and automatically hashes it to the right place.
        """
        for node in nodes:
            value = node.val.strip('\n')
            node.val = node.val.strip('\n')
            index = self.hash(value)
            location = self.nodes[index]
            if location == None:
                self.nodes[index] = node
            else:
                if location.pointer == None:
                    self.nodes[index].pointer = node
                else:
                    node.pointer = location.pointer
                    self.nodes[index].pointer = node

    def getNodes(self) -> list:
        """
        Returns a list of list of nodes in the hash table (using iteration).\n
        Note: the first node of each nested list is the first node of the corresponding linked list in the hash table.\n
        For example:\n
        >[["A", "Foo"], ["X", "Bar"]]\n
        The A and X here are the head of each linked list..
        """
        try:
            if len(self.nodes) < 1:
                # just pass
                pass
        except:
            print("Empty hash table")
            raise UserWarning("Empty hash table")
        final = []
        for li in self.nodes:
            buffer = []
            if li != None:
                while li.pointer != None:
                    buffer.append(li.val)
                    li = li.pointer
                buffer.append(li.val)
                final.append(buffer)
        return final

    def sort(self):
        """
        Sorts the nodes based on their value, it is done 
        """
        tmp0 = list(self.nodes)
        tmp1 = sorted(tmp0, key=lambda x: x.val)
        self.nodes = tmp1

    def __str__(self):
        res = "Hashtable: \n"
        if len(self.nodes) == 0:

            return "EMPTY HASH TABLE"
        counter = 0

        for i in self.nodes:
            buffer = ""
            iteration = i
            obj = i
            if iteration != None:
                if iteration.pointer == None:
                    buffer += f"| {self.nodes.index(i)} | <First & Only node> {iteration.val} \n"
                else:
                    tmp = ""
                    count = 0
                    while obj != None:
                        if count == 0:
                            tmp += f"| {self.nodes.index(i)} | <First node> {str(obj.val): <7}  -> ".format(
                            )
                        else:
                            tmp += f"{str(obj.val)} -> "
                        obj = obj.pointer
                        count += 1
                    tmp += "<END OF LINKED LIST>"
                    buffer += f"{tmp}\n"
                res += buffer
                counter += 1
        return res

    def lookup(self, target: Node):
        """
        Checks to see if the given node is indeed in the linked list\n
        Returns the index of that node if yes, returns False if not.
        """
        # print(f"Look up target value {target.val}")
        # print(f"Look up target hash value {self.hash(target.val)}")
        index = self.hash(target.val)
        if self.nodes[index] == None:
            return False
        if self.nodes[index].val == target.val:
            return index
        location = self.nodes[index]
        while location.pointer != None:
            location = location.pointer
            if location.val == target.val:
                return index
        return False

    def delete(self, target: Node):
        """
        Deletes an element from the hash table\n
        If the target node does not exist, return False
        """
        """
        res = self.lookup(target)
        if res == False:
            return False

        value = target.val
        current = self.nodes[res]
        if current.val == value:
            tmp.pointer = self.nodes[res].pointe
        while current.val != value:
            current = current.pointer
        """


# ========================================================================
