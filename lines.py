class Line:
    def __init__(self, asc=True):
        """init line asc or desc

        Parameters:
        asc -- ascending or descding order. (default = True)

        """
        self.stack = []
        self.asc = asc

    def stack_on(self, n):
        self.stack.append(n)

