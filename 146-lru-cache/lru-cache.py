class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, node: Node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        first.prev = node
        node.next = first

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.add(self.cache[key])
        elif key not in self.cache and len(self.cache) < self.capacity:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
        else:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)