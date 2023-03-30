class Stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, inputData):
        self.items.append(inputData)

    def pop(self):
        if self.items == []:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            return None
        else:
            return self.items[-1]
