class Calculation:
    result = None
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self):
        self.result = self.operation(self.x, self.y)
        return self.result
