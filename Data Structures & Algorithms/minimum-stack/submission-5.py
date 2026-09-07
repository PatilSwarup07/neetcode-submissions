class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        value=self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        return value
        

    def pop(self) -> None:
        value=self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
