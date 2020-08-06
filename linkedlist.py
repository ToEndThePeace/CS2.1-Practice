class Node:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def prepend(self, node):
        node.next = self.head
        self.head = node

    def append(self, node):
        if not self.head:
            # add node tp a zero-length list
            self.prepend(node)
        else:
            current = self.head
            while current is not None:
                current = current.next
            current.next = node
