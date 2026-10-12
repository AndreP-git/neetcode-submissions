class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        ans = self.array[self.length-1]
        self.array[self.length-1] = 0
        self.length -= 1
        return ans

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for idx, num in enumerate(self.array):
            new_array[idx] = num
        self.array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
