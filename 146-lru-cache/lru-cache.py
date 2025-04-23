class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        '''
        LL - double
        start -> LR node
        curr -> MR node
        lookup -> dict mapping from key -> LL node
        1. Get
        - check lookup, if present, return val for key. Delete that node, connect the rest, add new node
        in the front. Need doubly LL for O(1) deletion
        - if not present, -1
        2. PUT
        - check lookup, if present, update val. Delete that node, connect the rest, add new node
        in the front
        - if not, add node to front and update lookup. If cap exceeded, delete last node.
        '''
        self.capacity = capacity
        self.last = Node(-1,-1) # return next of last for LRnode
        self.curr = None
        self.lookup = defaultdict(Node)
        self.size = 0
    
    def deleteAndConnect(self,node):
        # delete this node, then add it to front
        # if node is curr, keep as is:
        if self.curr == node:
            return
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        newNode = Node(node.key, node.val)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        self.lookup[node.key] = newNode
        del node

    def get(self, key: int) -> int:
        
        if key in self.lookup:
            res = self.lookup[key].val
            self.deleteAndConnect(self.lookup[key])
            # print('GET:',self.lookup)
            return res
        # print('GET:',self.lookup)
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.lookup:
            # no need to check size
            node = self.lookup[key]
            node.val = value
            self.deleteAndConnect(self.lookup[key])
            # print('PUT:',self.lookup)
            return
        # add node
        if self.curr is None:
            self.curr = Node(key,value)
            self.lookup[key] = self.curr
            self.last.next = self.curr
            self.curr.prev = self.last
            self.size+=1
            if self.size>self.capacity:
                lastNode = self.last.next
                lastNode.next.prev = self.last
                self.last.next = lastNode.next
                del self.lookup[lastNode.key]
                del lastNode
                self.size-=1
        else:
            newNode = Node(key,value)
            self.lookup[key]= newNode
            self.curr.next = newNode
            newNode.prev = self.curr
            self.curr = newNode
            self.size+=1
            if self.size>self.capacity:
                lastNode = self.last.next
                lastNode.next.prev = self.last
                self.last.next = lastNode.next
                del self.lookup[lastNode.key]
                del lastNode
                self.size-=1
        # print('PUT:',self.lookup)
        return
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)