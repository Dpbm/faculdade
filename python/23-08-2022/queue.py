class Queue:
    def __init__(self):
        self.values = []
    
    def add(self, value):
        self.values.append(value)

    def de_queue(self):
        self.values = self.values[1:]
    

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(5)
queue.add(10)

print(queue.values)

queue.de_queue()

print(queue.values)

queue.de_queue()
queue.de_queue()

print(queue.values)