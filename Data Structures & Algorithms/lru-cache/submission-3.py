class Node:
    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.prev = None
        self.next = None    


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        prev.next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        self.right.prev = node
        prev.next = node
        node.next = self.right
        node.prev = prev
        

    def get(self, key: int) -> int:
        # O(1) time complexity, so a hashmap where key is key, val is the actual Node
        # if key is 
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # there should be a maintained pointer at the least recently used cache

        # if the hashset length >= LRU's capacity, remove the most recently used cache 
        if key in self.cache.keys():
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]

        newnode = Node(key, value)
        self.insert(newnode)

        self.cache[key] = newnode
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


