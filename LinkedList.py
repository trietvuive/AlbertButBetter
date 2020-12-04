class LinkedList:
    class Node:
        def __init__(self,start,end):
            if end<=start:
                raise Exception("You cannot end something before it starts")
            self.start = start
            self.end = end
            self.next = None
    def __init__(self):
        self.head = None
    def insert(self,start,end):
        return self.insert_node(LinkedList.Node(start,end))
    def insert_node(self,node):
        if self.overlap(node):
            return False
        if self.head is None:
            self.head = node
        elif node.end<self.head.start:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            while curr.next is not None and node.start < curr.next.end:
                curr = curr.next
            node.next = curr.next
            curr.next = node
        return True
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield (curr.start,curr.end)
            curr = curr.next
    def overlap(self,node):
        curr = self.head
        if self.head is None:
            return False
        while curr is not None and node.start >= curr.end :
            curr = curr.next
        if curr is None:
            return False
            #Can assume node.start > curr.prev.end
            if curr.start <= node.start or curr.start < node.end:
                return True
            return False
    def is_overlap(self,start,end):
        return self.overlap(LinkedList.Node(start,end))