"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
  """Represent a graph as a dictionary of vertices mapping labels to edges."""
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    """
    Add a vertex to the graph.
    """
    if self.vertices.get(vertex_id) is None:
      self.vertices[vertex_id] = set()

  def add_edge(self, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if self.vertices.get(v1) is None:
      raise Exception(v1)
    if self.vertices.get(v2) is None:
      raise Exception(v2)
    vert = self.vertices.get(v1)
    vert.add(v2)

  def get_neighbors(self, vertex_id):
    """
    Get all neighbors (edges) of a vertex.
    """
    verts = self.vertices.get(vertex_id)
    if verts is None:
      return None
    return verts

  def bft(self, starting_vertex):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    queue = Queue()
    queue.enqueue(starting_vertex)
    discovered = {starting_vertex}
    while queue.size() != 0:
      vertex = queue.dequeue()
      print(vertex)
      for edge in self.vertices.get(vertex):
        if edge not in discovered:
          discovered.add(edge)
          queue.enqueue(edge)

  def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    stack = Stack()
    stack.push(starting_vertex)
    discovered = {starting_vertex}
    while stack.size() != 0:
      vertex = stack.pop()
      print(vertex)
      for edge in self.vertices.get(vertex):
        if edge not in discovered:
          discovered.add(edge)
          stack.push(edge)

  def _dft_recursive(self, vertex, discovered):
    print(vertex)
    discovered.add(vertex)
    for edge in self.vertices.get(vertex):
      if edge not in discovered:
        self._dft_recursive(edge, discovered)

  def dft_recursive(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.

    This should be done using recursion.
    """
    discovered = set()
    self._dft_recursive(starting_vertex, discovered)

  def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    queue = Queue()
    queue.enqueue([starting_vertex])
    discovered = {starting_vertex}
    while queue.size() != 0:
      path = queue.dequeue()
      vertex = path[-1]
      if vertex == destination_vertex:
        return path
      for edge in self.vertices.get(vertex):
        if edge not in discovered:
          discovered.add(edge)
          new_path = list(path)
          new_path.append(edge)
          queue.enqueue(new_path)

  def dfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    stack = Stack()
    stack.push([starting_vertex])
    discovered = {starting_vertex}
    while stack.size() != 0:
      path = stack.pop()
      vertex = path[-1]
      if vertex == destination_vertex:
        return path
      for edge in self.vertices.get(vertex):
        if edge not in discovered:
          discovered.add(edge)
          new_path = list(path)
          new_path.append(edge)
          stack.push(new_path)

  def _dfs_recursive(self, path, destination_vertex, discovered, end_path):
    vertex = path[-1]
    if vertex == destination_vertex:
      for edge in path:
        end_path.append(edge)
    discovered.add(vertex)
    for edge in self.vertices.get(vertex):
      if edge not in discovered:
        new_path = list(path)
        new_path.append(edge)
        self._dfs_recursive(new_path, destination_vertex, discovered, end_path)

  def dfs_recursive(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.

    This should be done using recursion.
    """
    discovered = set()
    path = [starting_vertex]
    end_path = []
    self._dfs_recursive(path, destination_vertex, discovered, end_path)
    return end_path

if __name__ == '__main__':
  graph = Graph()  # Instantiate your graph
  # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
  graph.add_vertex(1)
  graph.add_vertex(2)
  graph.add_vertex(3)
  graph.add_vertex(4)
  graph.add_vertex(5)
  graph.add_vertex(6)
  graph.add_vertex(7)
  graph.add_edge(5, 3)
  graph.add_edge(6, 3)
  graph.add_edge(7, 1)
  graph.add_edge(4, 7)
  graph.add_edge(1, 2)
  graph.add_edge(7, 6)
  graph.add_edge(2, 4)
  graph.add_edge(3, 5)
  graph.add_edge(2, 3)
  graph.add_edge(4, 6)

  '''
  Should print:
    {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
  '''
  print(graph.vertices)

  '''
  Valid BFT paths:
    1, 2, 3, 4, 5, 6, 7
    1, 2, 3, 4, 5, 7, 6
    1, 2, 3, 4, 6, 7, 5
    1, 2, 3, 4, 6, 5, 7
    1, 2, 3, 4, 7, 6, 5
    1, 2, 3, 4, 7, 5, 6
    1, 2, 4, 3, 5, 6, 7
    1, 2, 4, 3, 5, 7, 6
    1, 2, 4, 3, 6, 7, 5
    1, 2, 4, 3, 6, 5, 7
    1, 2, 4, 3, 7, 6, 5
    1, 2, 4, 3, 7, 5, 6
  '''
  graph.bft(1)

  '''
  Valid DFT paths:
    1, 2, 3, 5, 4, 6, 7
    1, 2, 3, 5, 4, 7, 6
    1, 2, 4, 7, 6, 3, 5
    1, 2, 4, 6, 3, 5, 7
  '''
  graph.dft(1)
  graph.dft_recursive(1)

  '''
  Valid BFS path:
    [1, 2, 4, 6]
  '''
  print(graph.bfs(1, 6))

  '''
  Valid DFS paths:
    [1, 2, 4, 6]
    [1, 2, 4, 7, 6]
  '''
  print(graph.dfs(1, 6))
  print(graph.dfs_recursive(1, 6))
