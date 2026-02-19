class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.height = 1


class SetADT:
    def __init__(self):
        self.root = None

    # build(X) in O(n log n)
    def build(self, X):
        for element in X:
            self.insert(element)
    
    # insert(x) in O(lgn): Inserts and element in the set if it does not exists
    def insert(self, x):
        self.root = self._insert(self.root, x)
        
    # delete(k)in O(lg n): Delete element with key k if it exists
    def delete(self, k):
        self.root = self._delete(self.root, k)

    # find(k) in O(log n)
    def find(self, k):
        node = self.root
        while node:
            if k < node.element.key:
                node = node.left
            elif k > node.element.key:
                node = node.right
            else:
                return node.element

    # find_min() in O(log n)
    def find_min(self):
        node = self.root
        while node.left:
            node = node.left
        return node.element

    # find_max() in O(log n)
    def find_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.element

    # find_prev(k) in O(log n)
    def find_prev(self, k):
        node = self.root
        candidate = None
        while node:
            if node.element.key < k:
                candidate = node.element  
                node = node.right        
            else:
                node = node.left       
        return candidate 

            

    # find_next(k) in O(log n)
    def find_next(self, k):
        node = self.root
        candidate = None
        while node:
            if node.element.key > k:
                candidate = node.element  
                node = node.left        
            else:
                node = node.right       
        return candidate 
    
    def pre_order(self, node=None):
        if self.root == None:
            return
        if node == None:
            return
        self.pre_order(node.left)
        print(node.element.key, end=" ")
        self.pre_order(node.right)



    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y


    def _insert(self, node, element):
        if node == None:
            return Node(element)

        if element.key < node.element.key:
            node.left = self._insert(node.left, element)
        elif element.key > node.element.key:
            node.right = self._insert(node.right, element)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _delete(self, node, k):
        if not node:
            return None

        if k < node.element.key:
            node.left = self._delete(node.left, k)

        elif k > node.element.key:
            node.right = self._delete(node.right, k)

        else:
            # node found

            if not node.left:
                return node.right
            if not node.right:
                return node.left

            temp = self._min_node(node.right)
            node.element = temp.element
            node.right = self._delete(node.right, temp.element.key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node


    def _min_node(self, node):
        while node.left:
            node = node.left
        return node
        
e1 = Element(10, "A")
e2 = Element(20, "B")
e3 = Element(5, "C")
e4 = Element(15, "D")
e5 = Element(25, "E")
e6 = Element(13, "F")

my_set = SetADT()
my_set.build([e1, e2, e3, e4, e5])

print(my_set.root.right)
my_set.pre_order(my_set.root)  

print("")
my_set.insert(e6)
my_set.pre_order(my_set.root)  
print("")
my_set.delete(10)
my_set.pre_order(my_set.root)  
