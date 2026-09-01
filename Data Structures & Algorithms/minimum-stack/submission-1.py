class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, value: int) -> None:
        mv=self.getMin()
        if mv==None or mv>value:
            mv=value
        self.stack.append([value,mv])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None