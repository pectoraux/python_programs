'''
    Efficiency:  
    ----------------------------------------------
    member function union() of class UnionFind runs in O(n)
    isUndirected() runs in O(n^2)
    make_dict() runs in O(n)
    So question3() runs in O(n^2) 
'''

def question3(G):
    """
    Returns the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that iter(G) lists its
    vertices, iter(G[u]) lists the neighbors of u, G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    if not isUndirected(G):
        raise ValueError("MinimumSpanningTree: input is not undirected")
    for u in G:
        for v in G[u]:
            if G[u][v] != G[v][u]:
                raise ValueError("MinimumSpanningTree: asymmetric weights")

    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # Using UnionFind here since it makes Kruskal's algorithm, 
    # very simple to implement 
    subtrees = UnionFind()
    tree = {}
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            if u in tree:
                tree[u].append((v,W))
            else:
                tree[u] = [(v,W)]                   
            subtrees.union(u,v)    
    return tree

class UnionFind:
    """Union-find data structure.
    - X[item] returns a name for the set containing the given item.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.
    """
    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root    

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest    


def isUndirected(G):
    """Check that G represents a simple undirected graph."""
    for v in G:
        if v in G[v]:
            return False
        for w in G[v]:
            if v not in G[w]:
                return False
    return True

def make_dict(G1):
    """ Turns the values of a dictionary into dictionaries
        It's implementation makes the Kruskal's algorithm easier
    """
    keys = G1.keys()
    values = G1.values()
    new_values = [] 
    for u in values:
        new_values.append(dict(u))
    new_dict = dict(zip(keys, new_values))
    return new_dict 

def run():
        """Check that MinimumSpanningTree returns the correct answer."""
        # Test 1
        G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
        print question3(make_dict(G))
        # Test 2
        G1 = {'A': [('B', 10)],'B': [('A', 10), ('C', 2), ('D',3)], 'C': [('B', 2)], 'D':[('B',3)]}
        print question3(make_dict(G1))
        # Test 3
        G2 = {'A': [('B', 2), ('E',2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)], 'E':[('A',2)]}
        print question3(make_dict(G2))
        


if __name__ == "__main__":
    run()