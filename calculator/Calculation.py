class Calculation:
    result = None
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self):
        return self.operation(self.x, self.y)
    
    def __str__(self):
        return f"{self.operation} {self.x} and {self.y} = {self.result}"