''' 
    Makes a list of all the parent nodes in the tree with get_parents()
    then in LCA(), using the parents list previously computed
    goes from the first node n1 to the root and 
    after that, goes from the second node to the root,
    this time stopping as soon as a node already visited in the first 
    traversal is hit. That node would be the LCA.

'''

def get_parents(tree, parent): 
    for i in range(len(tree)):
        for j in range(len(tree[0])):
            if tree[i][j] == 1:
                parent[j] = i
               
def LCA(r, u, v, parent):
    '''
        Computes Least Common Ancestor of the nodes u and v
    '''
    lca = -1
    visited = [None for i in parent]
    
    '''
        Traverses from node u up to root node and mark the vertices 
        encountered along the path
    '''  
    while True:
        visited[u] = True
        if u == r:
            break;
        u = parent[u]
    '''
        Now traverses from node v and keeps going up until it 
        hits a node that is in the path of node u 
    '''   
    while True:
        ''' The first node it hits that is in visited is the lca '''
        if visited[v]:  
            lca = v
            break
        v = parent[v]
        
    return lca
            
def question4(T, r, n1, n2):
    '''
        Gets a list of all parent nodes in T and computes LCA
    '''
    parent = [ None for i in range(len(T))]
    get_parents(T, parent)
    print LCA(r, n1, n2, parent)

def run():
    # Test 1                            # Should return 3
    question4([[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]],
                3,
                1,
                4)
    # Test 2                            # Should return 1
    question4([[0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0]],
                1,
                1,
                3)
    # Test 3 -- lca between root and some node       # Should return root: 0
    question4([[0, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]],
                0,
                0,
                6)

if __name__ == '__main__':
       run()   