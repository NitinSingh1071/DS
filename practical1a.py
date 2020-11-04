class one_d:
    def __init__(self, ar):
        self.array = ar

    def search(self, e):
        if e in self.array:
            return True
        return False

    def sort(self):
        for i in range(len(self.array)):
            lowest_value_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[lowest_value_index]:
                    lowest_value_index = j
            self.array[i], self.array[lowest_value_index] = self.array[lowest_value_index], self.array[i]
        return self.array

    def merg(self,l):
        self.array = self.array + l
        return self.array

    def reverse(self):
        return self.array[::-1]

ar = [4,55,47,94,63,59,45,30]
b = one_d(ar)
print(b.sort())
print(b.search(63))
print(b.merg([15,26,57,90,74]))
print(b.reverse())

