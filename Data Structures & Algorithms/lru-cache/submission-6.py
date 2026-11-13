class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right, self.left = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def insert(self, node):
        # should always insert at the RIGHTMOST
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        
    def get(self, key: int) -> int:
        # if the key doesnt exist, -1
        # if it exists, return val,
            # REMOVE it from the current position in the Linked list
            # ADD it to the RIGHTmost position in the Linekd list
        
        if key not in self.cache.keys():
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        

    def put(self, key: int, value: int) -> None:
        # If exists, update value of key. If not, add to the hashmap
        # if the length of the hashmap exceeds the capacity, REMOVE leftmost node of linked list (and in the hashmap)
        # add the node to the RIGHTMOST position of the linked list
    
        if key in self.cache:
            self.remove(self.cache[key])


        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        
        while len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
