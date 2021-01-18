class Range:    
    def __init__(self, *args):
        self.start = 0 if len(args) == 1 else args[0]
        self.end = args[0] if len(args) == 1 else args[1]
            
    def __str__(self) -> str:
        return "[" + str(self.start) + ", " + str(self.end) + ")"
    
    def reset(self):
        self.start = self.end = 0

    def contains(self, item : int) -> bool:
        """
        Given a number/items it checks if the item/number 
        is present in the range or not
        """
        return self.start <= item and item < self.end
    
    def overlaps(self, range_obj) -> bool:
        """
        Checks if two ranges overlap by finding the 
        smaller lower bound of the two ranges and checking 
        whether the upper bound of the other range
        is greater or not
        """
        return range_obj.start < self.end if self.start < range_obj.start else self.start < range_obj.end

    def is_sub_range(self, range_obj) -> bool:
        """
        Checks if the range object is a sub-range of the 
        given super-range or not
        """
        return self.start >= range_obj.start and self.end <= range_obj.end

    def is_disjoint(self, range_obj) -> bool:
        """
        Returns True if the intersection of the ranges is Null
        """
        return not self.overlaps(range_obj)

    def is_touching(self, r) -> bool:
        """
        Returns True if the start of range object is equal 
        to the end of given range object or if the end of 
        range object is equal to the start of given range 
        object
        """
        return self.end == r.start or self.start == r.end
    
    def combine(self, range_obj) -> bool:
        """
        Returns a new Range object which is a combination of 
        the two ranges if they are not disjoint
        """
        if self.is_disjoint(range_obj):
            return Range(0)

        new_start = min(self.start, range_obj.start)
        new_end = max(self.end, range_obj.end)
        return Range(new_start, new_end)

    def is_equal_to(self, range_obj) -> bool:
        """
        Returns True if the starting and ending points are equal
        """
        return self.start == range_obj.start and self.end == range_obj.end
    
    def is_less_than(self, range_obj) -> bool:
        """
        If both the range objects have same starting points,
        returns True if range_obj ends before the present 
        object
        """
        return self.end < range_obj.end if self.start == range_obj.start else self.start < range_obj.start and self.end < range_obj.end
    
    def is_more_than(self, range_obj) -> bool:
        """
        If both the range objects have same starting points,
        returns True if range_obj starts before the present 
        object
        """
        return self.end > range_obj.end if self.start == range_obj.start else self.start > range_obj.start and self.end > range_obj.end
    
    def length(self) -> int:
        """
        Returns length of the Range
        """
        return self.end - self.start
    
    def shift(self, n: int) -> None:
        """
        Shifts Range by n by adding n to the limits
        """
        self.start += n
        self.end += n

        if self.start > self.end:
            self.reset()
    
    def rshift(self, n: int) -> None:
        """
        Shifts ending point of Range by n
        """
        self.end += n
        if self.start > self.end:
            self.reset()
    
    def lshift(self, n: int) -> None:
        """
        Shifts starting point of Range by n
        """
        self.start += n
        if self.start > self.end:
            self.reset()
    
    def squeeze(self, n: int) -> None:
        """
        Changes Range by increasing lower limit by n 
        and decreasing upper limit by n
        """
        self.start += n
        self.end -= n

        if self.start > self.end:
            self.reset()
    
    def stretch(self, *args) -> None:
        """
        Changes Range by stretching the limits
        """
        left = args[0]
        right = args[0] if len(args) == 1 else args[1]

        self.start -= left
        self.right += right

        if self.start > self.end:
            self.reset()