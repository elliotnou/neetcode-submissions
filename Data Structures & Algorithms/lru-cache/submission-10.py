class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def insert(self, node):
        node.prev = self.left
        node.next = self.left.next
        node.next.prev = node
        self.left.next = node


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
        

    def get(self, key: int) -> int:
        # find value of key in self.cache
        # remove that node from the LRU linked list
        # add it back to the LEFT
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        # if key exists, update the val of key and remove and insert
        # if key doesn't exist, ADD key-val to self.cache AND insert to linked list
            # if this causes cache to exceed capacity, remove the leftmost node and delete from self.cache

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            while len(self.cache) > self.capacity:
                node = self.right.prev
                self.remove(node)
                del self.cache[node.key]

        
