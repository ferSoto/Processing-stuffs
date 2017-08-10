# Edge class


from random import randint


class Edge:
    def __init__(self, node_a, node_b):
        self._a = node_a
        self._b = node_b
        self._weight = randint(1, 100007)
        
    def __cmp__(self, other):
        return cmp(self.weight, other.weight)
        
    def a(self):
        return self._a
    
    def b(self):
        return self._b

    def weight(self):
        return self._weight