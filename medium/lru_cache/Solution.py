# from collections import OrderedDict
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.max_size = capacity
#         self.data = OrderedDict()

#     def get(self, key: int) -> int:
#         if key in self.data:
#             self.data.move_to_end(key)
#             return self.data[key]
#         else:
#             return -1
        
#     def put(self, key: int, value: int) -> None:
#         if len(self.data) == self.max_size:
#             self.data.popitem(last=False)
        
#         self.data[key] = value

class Node:
  def __init__(self, key, value):
    self.key, self.value = key, value
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {} # {key: Node}
    self.head = Node(0, 0) # dummy
    self.tail = Node(0, 0) # dummy
    
    # head=LRU, tail=most recent
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def remove(self, node: Node):
    node.prev.next = node.next
    node.next.prev = node.prev

  def insert_end(self, node: Node):
    prev = self.tail.prev
    nxt = self.tail
    prev.next = node
    nxt.prev = node
    node.next = nxt
    node.prev = prev

  def get(self, key: int):
    if key in self.cache:
      # becomes most recently accessed
      lru_node = self.cache[key]
      self.remove(lru_node)
      self.insert_end(lru_node)
      return lru_node.value
    else:
      return -1

  def put(self, key: int, value: int):
    if key in self.cache:
        self.remove(self.cache[key])
    
    # pointer to a Node
    self.cache[key] = Node(key, value)
    self.insert_end(self.cache[key])

    # check if capacity reached
    if len(self.cache) > self.capacity:
      lru = self.head.next
      self.remove(lru)
      # remove from cache
      del self.cache[lru.key]