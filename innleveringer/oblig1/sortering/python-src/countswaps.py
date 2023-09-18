class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]
    
    #egendefinert hjelpemetode for mergesort
    def increase_swaps(self, i:int):
        self.swaps +=i
    def get_swaps(self):
        return self.swaps
