class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        
    def pushback(self, n: int) -> None:
        self.size += 1
        self.arr.append(n)
        if self.size > self.capacity:
            self.resize()

    def popback(self) -> int:
        if self.capacity <= 1:
            return
        self.size -= 1
        pop = self.arr[-1]
        del self.arr[-1]
        return pop

    def resize(self) -> None:
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
