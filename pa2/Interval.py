class Interval():
    #Class representing an interval of numbers [low, high]

    def __init__(self, low, high):
        #Initialize the Interval object with low and high values
        if low > high:
            raise SyntaxError("empty interval")
        self.low = low
        self.high = high

    def __str__(self):
        #Return a string representation of the Interval object
        return f"Interval({self.low}, {self.high})"

    def __add__(self, other):
        #Add two Interval objects and return the result as a new Interval object
        return Interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        #Subtract two Interval objects and return the result as a new Interval object.
        return Interval(self.low - other.high, self.high - other.low)

    def __mul__(self, other):
        #Multiply two Interval objects and return the result as a new Interval object.
        a = min(self.low * other.low, self.low * other.high, self.high * other.low, self.high * other.high)
        b = max(self.low * other.low, self.low * other.high, self.high * other.low, self.high * other.high)
        return Interval(a, b)

    def __truediv__(self, other):
        #Divide two Interval objects and return the result as a new Interval object
        if other.low <= 0 <= other.high:
            raise ZeroDivisionError("interval division by zero")
        a = min(self.low / other.low, self.low / other.high, self.high / other.low, self.high / other.high)
        b = max(self.low / other.low, self.low / other.high, self.high / other.low, self.high / other.high)
        return Interval(a, b)
    
    def intersect(self, other):
        #takes two intervals and returns its intersection as a new Interval object
        if self.low > other.high or other.low > self.high:
            raise SyntaxError("Intervals do not intersect.")
        
        return Interval(max(self.low, other.low), min(self.high, other.high))
    
    def intersects(self, other):
        #Is a basic true or false test to see if two intervals intersect
        if self.low > other.high or other.low > self.high:
            return False
        
        return True
    
    def union(self, other):
        #Return the union of two Interval objects as a new Interval object
        return Interval(min(self.low, other.low), max(self.high, other.high))
    
    def __eq__(self, other):
        #Return True if two Interval objects are equal
        return self.low == other.low and self.high == other.high