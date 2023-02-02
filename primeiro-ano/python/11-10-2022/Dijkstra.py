class Node:
    def __init__(self, neighbors=[]):
        self.visited = False
        self.value = None
        self.neighbors = neighbors

class Dijkstra:
    def __init__(self, start_node):
        self.actual_node = start_node
        self.nodes_queue = []        

    def get_neighbor_shortest_path(self):
        sort_neighbors = lambda neighbor: neighbor[1].value  

        distances = sorted(self.actual_node.neighbors, key=sort_neighbors)

        self.actual_node = distances[0][1]
        self.nodes_queue = distances
        

    def map_neighbors(self, node):
        for neighbor_distance, neighbor_node in node.neighbors:
            neighbor_node.value = self.calc_neighbor_distance(distance, neighbor_node)

    def calc_neighbor_distance(self, distance, neighbor_node):        
        if(neighbor_node.visited):
            return neighbor_node.value

        new_neighbor_distance_value = distance + self.actual_node.value 
        neighbor_node.visited = True

        if(not neighbor_node.value or neighbor_node.value > new_neighbor_distance_value)
            return new_neighbor_distance_value

        return neighbor_node.value
    



n1 = Node()
n2 = Node()
n3 = Node()

n1.neighbors = ((4, n2), (4, n3))
n2.neighbors = ((4, n1), (2, n3))
n3.neighbors = ((2, n2), (4, n1))
