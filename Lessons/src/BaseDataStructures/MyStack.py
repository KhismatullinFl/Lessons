class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        if self.queue1:
            while self.queue1:
                self.queue2.append(self.queue1[0])
                del self.queues1[0]
        self.queue1.append(x)
        if self.queue2:
            while self.queue2:
                self.queue1.append(self.queue2[0])
                del self.queue2[0]
    def pop(self):
        i = self.queue1[0]
        del self.queue1[0]
        return i

    def top(self):
        return self.queue1[0]

    def empty(self):
        return bool(not self.queue1)