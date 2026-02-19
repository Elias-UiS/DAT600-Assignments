class DisjointSetElement:
    def __init__(self, key):
        self.key = key
        self.parent = self      
        self.rank = 0           


class DisjointSet:
    def make_set(self, x):
        return DisjointSetElement(x)

    def find_set(self, x):
        if x.parent != x:
            x.parent = self.find_set(x.parent)  
        return x.parent

    def union(self, x, y):
        x_root = self.find_set(x)
        y_root = self.find_set(y)

        if x_root == y_root:
            return  

        if x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root.rank > y_root.rank:
            y_root.parent = x_root
        else:
            y_root.parent = x_root
            x_root.rank += 1
