class Line:
    def __init__(self, asc):
        """
        asc -- ascend or descend line
        """
        self.stack = []
        self.asc = asc

    def stack_on(self, n):
        self.stack.append(n)
