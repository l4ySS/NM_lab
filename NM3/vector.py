from math import sqrt


def make_vector(_L):
    vector = Vector([0]*_L)
    return vector


class Vector:
    def __init__(self, _nums=None):
        if _nums is None:
            _nums = []
        self.nums = _nums
        self.size = len(_nums)

    def set(self, L):
        self.nums = [0]*L
        self.size = L
        return self

    def __getitem__(self, index):
        return self.nums[index - 1]

    def __setitem__(self, index, value):
        self.nums[index - 1] = value

    def __repr__(self):
        return '\t'.join(str(x) for x in self.nums)

    def __len__(self):
        return len(self.nums)

    def __add__(self, other):
        new = []
        for i in range(self.size):
            new.append(self.nums[i]+other.nums[i])
        return Vector(new)

    def __sub__(self, other):
        new = []
        for i in range(self.size):
            new.append(self.nums[i] - other.nums[i])
        return Vector(new)

    def __eq__(self, other):
        return self.nums == other.nums

    def norm(self):
        return abs(max(self.nums, key=abs))

    def normalize(self):
        mod = 0
        for i in range(1, self.size+1):
            mod += self[i] * self[i]
        for i in range(1, self.size + 1):
            self[i] = self[i] / sqrt(mod)
        return self

    def dot_product(self, other):
        return sum([self.nums[i]*other.nums[i] for i in range(self.size)])

    def sort(self):
        self.nums.sort()
        return self



