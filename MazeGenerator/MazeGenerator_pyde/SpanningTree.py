# Spanning Tree class


import heapq


class SpanningTree:
    def __init__(self, edge_list, nodes_per_row):
        # Create heap/priority queue from edge list
        self._priority_queue = heapify(edge_list)
        self._nodes_per_row = nodes_per_row
        
        # Parent list
        self._parents = [x for x in range(0, nodes_per_row * nodes_per_row)]
        
        # List with tree edges
        self._tree_edges = []
        self.create_tree()
        
    def _create_tree(self):
        pass
        
    def _find_set(self, node):
        if self._parents[node] != node:
            # If this node isn't its own father, keep searching
            self._parents[node] = self._find_set(self._parents[node])
        return node
    
    def _find_sets(self, node_a, node_b):
        return self._find_set(node_a), self._find_set(node_b)
        
    def _join_sets(self, edge):
        set_a, set_b = self._find_sets(edge.a, edge.b)
        
        # If nodes belong to different sets, join them
        if set_a == set_b: return
        self._parents[node_b] = node_a
        
    def _tree_is_finished(self):
        # The spanning tree is finished when there is one, and only one set remaining
        current_set = self._parents[0]
        for parent in self._parents:
            if parent != current_set:
                return False
            
        return True