class Line:
    def __init__(self):
        """init line asc or desc

        Parameters:
        asc -- ascending or descding order. (default = True)

        """
        self.stack = []

    def stack_on(self, n):
        self.stack.append(n)
        self.top = n

    def valid_stack(self, n):
        pass


class AscLine(Line):
    def __init__(self):
        self.stack = [1]
        self.top = 1

    def valid_stack(self, n):
        if n > self.top:
            return True
        elif self.top - n == 10:
            return True

        return False


class DescLine(Line):
    def __init__(self):
        self.stack = [99]
        self.top = 99

    def valid_stack(self, n):
        if n < self.top:
            return True
        elif n - self.top == 10:
            return True

        return False
