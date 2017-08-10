# Edge class

class Edge:
    def __init__(self, nodeA, nodeB):
        self._a = nodeA
        self._b = nodeB
        
    def a(self):
        return self._a
    
    def b(self):
        return self._b