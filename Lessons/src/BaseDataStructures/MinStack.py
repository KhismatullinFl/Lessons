class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, val):
        self.stack1.append(val)
        if ((self.stack2) and (self.stack2[-1] >= val)):
            self.stack2.append(val)
        if(not self.stack2):
            self.stack2.append(val)
    def pop(self):
        if (self.stack2[-1]==self.stack1[-1]):
            self.stack2.pop()
        return self.stack1.pop()
    def top(self):
        return self.stack1[-1]
    def getMin(self):
        return self.stack2[-1]