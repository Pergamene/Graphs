from collections import deque

class FamilyTree:
  def __init__(self, family_data):
    self.vertices = {}
    for parent, child in family_data:
      self.add_connection(child, parent)

  def add_connection(self, child, parent):
    if self.vertices.get(child) is None:
      self.vertices[child] = {parent}
    else:
      self.vertices.get(child).add(parent)

  def find_all_paths(self, child):
    all_paths = []
    queue = deque()
    queue.append([child])
    while len(queue) != 0:
      path = queue.popleft()
      vertex = path[-1]
      parents = self.vertices.get(vertex)
      if parents is None:
        all_paths.append(path)
      else:
        for parent in parents:
          new_path = list(path)
          new_path.append(parent)
          queue.append(new_path)
    return all_paths

  def find_longest_path(self, paths):
    longest = 0
    longest_path = []
    for path in paths:
      if len(path) > longest:
        longest = len(path)
        longest_path = path
      elif len(path) == longest:
        if path[-1] < longest_path[-1]:
          longest_path = path
    return longest_path

  def has_parents(self, child):
    if self.vertices.get(child) is None:
      return False
    return True

def earliest_ancestor(ancestors, starting_node):
  family_tree = FamilyTree(ancestors)
  if not family_tree.has_parents(starting_node):
    return -1
  paths = family_tree.find_all_paths(starting_node)
  longest_path = family_tree.find_longest_path(paths)
  return longest_path[-1]
