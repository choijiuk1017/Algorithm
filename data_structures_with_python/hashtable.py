class HashTable:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.__table = [None]* maxSize
        self.__numItems = 0
        self.__deleted = (None, None)
        
    def __hash(self, key):
        return key % self.maxSize
        
    def insert(self, key, value):
        hash = self.__hash(key)
        if not self.__table[hash] or self.__table[hash] == self.__deleted:
            self.__table[hash] = (key, value)
            self.__numItems += 1
            return
        # collision detected
        hash = (hash + 1) % self.maxSize
        numTrials = 0
        while numTrials < self.maxSize and self.__table[hash]:
            hash = (hash + 1) % self.maxSize
            numTrials += 1
        if numTrials == self.maxSize:
            print(f"insertion ({key}, {value}) failed")
            return
        self.__table[hash] = (key, value)
        self.__numItems += 1        
        
    def search(self, key):
        hash = self.__hash(key)
        if not self.__table[hash]:
            return None
        if self.__table[hash][0] != key:
            hash = (hash + 1) % self.maxSize
            numTrials = 0
            while numTrials < self.maxSize and self.__table[hash] and self.__table[hash][0] != key:
                hash = (hash + 1) % self.maxSize
                numTrials += 1
            if numTrials == self.maxSize:
                return None
            if not self.__table[hash]:
                return None
            # FALL THROUGH
        return self.__table[hash][1]
    
    def delete(self, key):
        hash = self.__hash(key)
        if not self.__table[hash]:
            return
        if self.__table[hash][0] != key:
            hash = (hash + 1) % self.maxSize
            numTrials = 0
            while numTrials < self.maxSize and self.__table[hash] and self.__table[hash][0] != key:
                hash = (hash + 1) % self.maxSize
                numTrials += 1
            if numTrials == self.maxSize:
                return
            if not self.__table[hash]:
                return
            # FALL THROUGH
        self.__table[hash] = self.__deleted
        self.__numItems -= 1            
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def clear(self):
        self.__table.clear()
        self.maxSize = 0
        self.__numItems = 0
        
    def print(self):
        for idx, item in enumerate(self.__table):
            if not item: continue
            print(f"[{idx}]: ({item[0]}, {item[1]})")
        
if __name__ == "__main__":
    h = HashTable(13)
    h.insert(1, "Goblin")
    h.insert(100, "Healer")
    h.insert(32, "Wizard")    
    h.insert(7, "Wizard3")
    h.insert(6, "Wizard2")
    h.print()
    
    print(f"searching for 100 returns {h.search(100)}")
    h.print()
    print(f"searching for 6 returns {h.search(6)}")
    h.delete(100)
    #h.delete(6)
    h.delete(7)
    h.print()
    print(f"searching for 6 returns {h.search(6)}")
    print(f"searching for 100 returns {h.search(100)}")
    