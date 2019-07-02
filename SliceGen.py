class SliceGen:
    """creates a generator to slice indexable objects
    example:
    nums = [1,2,3,4,5,6,7]
    x = iter(SliceGen(nums, 1, 6, 2))
    print(next(x))
    ...etc
    """
    def __init__(self, obj, start=0, stop=None, step=1):
        self.start = start
        if not stop:
            self.stop = len(obj)
        else:
            self.stop = stop
        self.step = step
        self.obj = obj
    
    def __iter__(self):
        index = self.start
        while index < self.stop:
            yield self.obj[index]
            index += self.step
