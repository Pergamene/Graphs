from collections import deque

class GraphWalker:
  def __init__(self):
    self.path = []
    self.map = {}
    self.unexplored_paths = 0
  
  def walk(self, player):
    self._walk_to_end(player.current_room)
    return self.path

  def _walk_to_end(self, starting_room):
    self._fill_map(starting_room)
    room = starting_room
    while self.unexplored_paths > 0:
      direction = self._get_walk_direction(room)
      if direction is not None:
        room = self._walk(room, direction)
      else:
        room = self._walk_back(room)

  def _fill_map(self, room):
    if room.id not in self.map:
      exit_map = {}
      for room_exit in room.get_exits():
        exit_map[room_exit] = '?'
        self.unexplored_paths += 1
      self.map[room.id] = exit_map

  def _get_map(self, room):
    return self.map[room.id]

  def _walk(self, room, direction):
    second_room = room.get_room_in_direction(direction)
    self._fill_map(second_room)
    self._add_connection(room, direction, second_room)
    self.path.append(direction)
    return second_room

  def _get_walk_direction(self, room):
    room_map = self._get_map(room)
    if 'n' in room_map and room_map['n'] == '?':
      return 'n'
    elif 'e' in room_map and room_map['e'] == '?':
      return 'e'
    elif 's' in room_map and room_map['s'] == '?':
      return 's'
    elif 'w' in room_map and room_map['w'] == '?':
      return 'w'
    else:
      return None

  def _walk_back(self, starting_room):
    room_queue = deque()
    path_queue = deque()
    room_queue.append([starting_room])
    path_queue.append([''])
    while len(room_queue) != 0:
      rooms = room_queue.popleft()
      room = rooms[-1]
      path = path_queue.popleft()
      if self._get_walk_direction(room) is not None:
        for move in range(1, len(path)):
          self.path.append(path[move])
        return room
      else:
        room_map = self._get_map(room)
        for direction in room.get_exits():
          if room_map[direction] is not None:
            new_rooms = list(rooms)
            new_path = list(path)
            new_rooms.append(room.get_room_in_direction(direction))
            new_path.append(direction)
            room_queue.append(new_rooms)
            path_queue.append(new_path)

  def _add_connection(self, first_room, direction, second_room):
    first_map = self._get_map(first_room)
    second_map = self._get_map(second_room)
    if direction == 'n':
      first_map['n'] = second_room.id
      second_map['s'] = first_room.id
    elif direction == 's':
      first_map['s'] = second_room.id
      second_map['n'] = first_room.id
    elif direction == 'e':
      first_map['e'] = second_room.id
      second_map['w'] = first_room.id
    else:
      first_map['w'] = second_room.id
      second_map['e'] = first_room.id
    self.unexplored_paths -= 2
        