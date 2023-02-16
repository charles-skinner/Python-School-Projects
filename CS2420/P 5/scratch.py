class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert_after(self, value):
        if value < self.value:
            if self.left:
                self.left.insert_after(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.insert_after(value)
            else:
                self.right = Node(value)
        else:
            raise ValueError("this tree doesn't accept duplicates")

    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class Binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self.root.insert_after(value)

    def __repr__(self):
        return repr(self.root)

bst = Binary_search_tree()
for x in range(100):
    bst.insert(x)

print(str(bst))


