class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def set_parent(self, node):
        self.parent = node

    def add(self, data):
        node = Node(data)
        node.set_parent(self)

        self.children.append(node)

        return node

    def size(self):
        return sum([c.size() for c in self.children]) + 1

    def depth(self):
        s = 0
        target = self
        
        while target.parent:
            s += 1
            target = target.parent

        return s

class Tree:
    def __init__(self, node):
        self.root = node

    def traverse(self, node):
        for num, c in enumerate(node.children):
            print(f"{c.depth() - 1}.{num} {c.data}")
            self.traverse(c)
