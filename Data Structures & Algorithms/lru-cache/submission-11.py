class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    # 정의: LRU is on LEFT, MRU is on RIGHT. insert should add to RIGHT.

    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
        self.cache = {}


    def get(self, key: int) -> int:
        # if key exists, returnt he value of key and remove node and insert
        # if key doesnt exist, return -1.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, udpate its value, remove node, insert node
        # if key doesnt exist, add the cache, insert node
            # if length of cache exceeds capacity, remove the LEFTMOST and delete from cache.
        newnode = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = newnode
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        
