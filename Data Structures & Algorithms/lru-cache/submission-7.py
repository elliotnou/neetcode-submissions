class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # intialize the cache, as well as the linked list left and right
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        prev.next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
        else:
            self.cache[key].val = value
            self.remove(self.cache[key])
        
        self.insert(self.cache[key])
        while len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
