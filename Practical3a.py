class Stack:
    def __init__(self):
        self.data = []

    def Empty(self):
        self.len_data = len(self.data)
        return self.len_data

    def push(self,elememt):
        self.data.append(elememt)

    def pop(self):
        if self.Empty():
            print("Empty Array")
        else:
            self.data.pop()

    def TopElement(self):
        print("Top element : ",self.data[-1])

    def display(self):
        print(self.data)
        print(self.Empty())

Stack_Operation = Stack()
Stack_Operation.push(20)
Stack_Operation.push(65)
Stack_Operation.push(33)
Stack_Operation.display()
Stack_Operation.TopElement()
Stack_Operation.pop()
Stack_Operation.display()
Stack_Operation.pop()
Stack_Operation.pop()
Stack_Operation.display()
Stack_Operation.pop()



