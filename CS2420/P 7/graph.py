import math


"""
docstring
"""
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.vertex_info = {}

    def add_vertex(self,label):
        """
        add a vertex with the specified label. Return the graph. label must be a
        string or raise ValueError
        """
        if isinstance(label,str) is False:
            raise ValueError

        self.adjacency_list[label] = []
        return self


    def add_edge(self,src,dest,w):
        """
        add an edge from vertex src to vertex dest with weight w. Return
        the graph. validate src, dest, and w: raise ValueError if not valid.
        """
        if (isinstance(w,float)) is False:
            if isinstance(w,int):
                float(w)
            else:
                raise ValueError

        self.edge_weights[(src,dest)] = w
        try:
            self.adjacency_list[dest]
            self.adjacency_list[src].append(dest)
        except:
            raise ValueError
        return self


    def get_weight(self,src,dest) :
        """
        Return the weight on edge src-dest (math.inf if no path exists,
        raise ValueError if src or dest not added to graph).
        """
        try:
            self.adjacency_list[src]
            self.adjacency_list[dest]
        except:
            raise ValueError

        try:
            return self.edge_weights[(src,dest)]
        except:
            return math.inf


    def dfs(self,starting_vertex):
        """
        Return a generator for traversing the graph in depth-first order
        starting from the specified vertex. Raise a ValueError if the vertex does not exist.
        """
        stack = [starting_vertex]
        visited_set = set()

        while len(stack) > 0:
            current = stack.pop()
            if current not in visited_set:
                yield current
                visited_set.add(current)
                for adjacent in self.adjacency_list[current]:
                    stack.append(adjacent)

    def bfs(self,starting_vertex):
        """
        Return a generator for traversing the graph in breadth-first order
        starting from the specified vertex. Raise a ValueError if the vertex does not exist.
        """
        discovered = set(starting_vertex)
        frontier = [starting_vertex]

        while frontier:
            current = frontier.pop(0)
            yield current
            for adjacent in self.adjacency_list[current]:
                if adjacent not in discovered:
                    frontier.append(adjacent)
                    discovered.add(adjacent)

    def dsp(self,src,dest):
        """
        Return a tuple (path length , the list of vertices on the path from dest
        back to src). If no path exists, return the tuple (math.inf,  empty list.)
        """
        vertexes = {}
        unvisited = []
        for vertex in self.adjacency_list:
            vertexes[vertex] = [math.inf,None]
            unvisited.append(vertex)
        vertexes[src][0] = 0
        while len(unvisited) > 0:
            smallest_index = 0
            for i in range(1,len(unvisited)):
                if vertexes[unvisited[i]][0] < vertexes[unvisited[smallest_index]][0]:
                    smallest_index = i
            current = unvisited.pop(smallest_index)

            for adjacent in self.adjacency_list[current]:
                weight = self.edge_weights[(current,adjacent)]
                alt = vertexes[current][0] + weight

                if alt < vertexes[adjacent][0]:
                    vertexes[adjacent][0] = alt
                    vertexes[adjacent][1] = current

        path = []
        current = dest
        while current != src:
            path.insert(0,current)
            current = vertexes[current][1]
            if current is None:
                return (math.inf,[])
        path.insert(0,src)
        return (vertexes[dest][0],path)
        

    def dsp_all(self,src):
        """
        Return a dictionary of the shortest weighted path between src and all
        other vertices using Dijkstra's Shortest Path algorithm. In the dictionary, the key is the the
        destination vertex label, the value is a list of vertices on the path from src to dest inclusive. 
        """
        vertexes = {}
        unvisited = []
        for vertex in self.adjacency_list:
            vertexes[vertex] = [math.inf,None]
            unvisited.append(vertex)
        vertexes[src][0] = 0
        while len(unvisited) > 0:
            smallest_index = 0
            for i in range(1,len(unvisited)):
                if vertexes[unvisited[i]][0] < vertexes[unvisited[smallest_index]][0]:
                    smallest_index = i
            current = unvisited.pop(smallest_index)

            for adjacent in self.adjacency_list[current]:
                weight = self.edge_weights[(current,adjacent)]
                alt = vertexes[current][0] + weight

                if alt < vertexes[adjacent][0]:
                    vertexes[adjacent][0] = alt
                    vertexes[adjacent][1] = current

        result = {}
        for vertex in self.adjacency_list:
            path = []
            current = vertex
            while current != src:
                path.insert(0,current)
                current = vertexes[current][1]
                if current == None:
                    break
            path.insert(0,src)
            result[vertex] = path
        return result


    def __str__(self):
        """
        Produce a string representation of the graph that can be used with print(). The
        format of the graph should be in GraphViz
        """
        output = "digraph G {\n"
        for vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                output += "   " + vertex + " -> " + adjacent
                output += f" [label=\"{self.edge_weights[(vertex,adjacent)]}\""
                output += f",weight=\"{self.edge_weights[(vertex,adjacent)]}\"];\n"
        output += "}\n"
        return output

def main():
    """
    docstring
    """
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A","B",2.0) 
    g.add_edge("A","F",9.0)
    g.add_edge("B","C",8.0)
    g.add_edge("B","D",15.0)
    g.add_edge("B","F",6.0)
    g.add_edge("C","D",1.0)
    g.add_edge("E","C",7.0)
    g.add_edge("E","D",3.0)
    g.add_edge("F","B",6.0)
    g.add_edge("F","E",3.0)
    print(g)
    print("starting BFS with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end = "")
    print()
    print("starting DFS with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end = "")
    print()
    for vertex in g.dsp("A","F")[1]:
        print(vertex, end = "")
    print()
    result = g.dsp_all("A")
    for key in result:
        for vertex in result[key]:
            print(vertex,end = "")
        print()
    print()

if __name__ == "__main__":
    main()
