class _UniNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLink:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = _UniNode(data)
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

        return

    def get_data(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.data)
            current = current.next

        return vals

class _BiNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLink:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = _BiNode(data)
        if self.head is None:
            self.head = node

        elif self.tail is None:
            self.tail = node
            self.tail.previous = self.head
            self.head.next = node

        else:
            self.tail.next = node
            node.previous = self.tail

        return
