class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def insert(self, node):
        node.next = self.left.next
        node.next.prev = node
        self.left.next = node
        node.prev = self.left

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache.keys()) > self.cap:
                node = self.right.prev
                self.remove(node)
                del self.cache[node.key]



        
