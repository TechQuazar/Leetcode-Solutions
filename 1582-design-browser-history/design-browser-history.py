class Node:
    def __init__(self, home):
        self.val = home
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(homepage)
        self.curr = self.root
    def clearNext(self):
        prev = self.curr.next
        curr = prev.next

        while curr!=None:
            del prev
            prev = curr
            curr = curr.next
        
        if curr==None:
            del prev
        return
        

    def visit(self, url: str) -> None:
        node = Node(url)
        if self.curr.next!=None:
            self.clearNext() # clears dangling
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        

    def back(self, steps: int) -> str:
        while steps>0:
            if self.curr.prev!=None:
                self.curr = self.curr.prev
            else:
                break
            steps-=1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps>0:
            if self.curr.next!=None:
                self.curr = self.curr.next
            else:
                break
            steps-=1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)