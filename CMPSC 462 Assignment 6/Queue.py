class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, inputData):
        self.items.append(inputData)

    def dequeue(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop(0)
