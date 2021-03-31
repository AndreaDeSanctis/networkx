"""greedy-search algorithm for shortest paths. """

import networkx as nx
import numpy as np

def greedy_path(G ,source, target, heuristic=None, weight='weight'):
    
    """check if the given source is in the given graph"""
    if source not in G:
        print("Source node is not in G")
        raise nx.NodeNotFound()
    
    current = source
    path = []
    
    while True:
        """check if the target is reached"""
        if current == target:
            path.append(current)
            return path
        
        """append the visited node"""
        path.append(current)
        
        """get the neighbors of current node by filtering them about who's
            already in 'path' """
        neighbors = list(G[current])
        filtered = []
        for i in neighbors:
            if i not in path:
                filtered.append(i)
        
        """check if there are neighbors to build the path"""
        if len(filtered) == 0:
            print(target + " node unreachable from " + source)
            raise nx.NetworkXNoPath()
        
        """choosing the best current node using the heuristic"""
        node_index = np.argmin(list(map(lambda x: heuristic(x, target), filtered)))
        current = filtered[node_index]
        