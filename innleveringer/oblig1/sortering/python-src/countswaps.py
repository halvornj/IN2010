class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]
    

    #hvorfor er CountSwaps subklasse av list, og ikke en fancy wrapper??
    #egendefinert hjelpemetode for mergesort
    def set_swaps(self, sum:int):
        self.swaps +=sum
    def get_swaps(self):
        return self.swaps
