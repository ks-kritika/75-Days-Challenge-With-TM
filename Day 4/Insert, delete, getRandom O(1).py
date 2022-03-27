class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.vals))
        