from vector import *


def make_matrix(_N, _L):
    vectors = []
    for i in range(_N):
        vectors.append(make_vector(_L))
    return Matrix(vectors)


class Matrix:
    def __init__(self, _data=None):
        if _data is None:
            _data = Vector()
        self.data = _data
        self.N = len(self.data)
        if not self.data:
            self.L = self.data.size
        else:
            self.L = self.data[0].size

    def set(self, _N=0, _L=0):
        self.data = [Vector.set(Vector(), _L)]*_N
        self.N = _N
        self.L = _L

    def __len__(self):           # N
        return len(self.data)

    def l(self):               # L
        return len(self.data[0])

    def __getitem__(self, pos):
        i, j = pos
        return self.data[i-1][j]

    def __setitem__(self, pos, value):
        i, j = pos
        self.data[i-1][j] = value

    def __repr__(self):
        return '\n'.join(str(x) for x in self.data)

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i]+other.data[i])
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] - other.data[i])
        return Matrix(result)

    def __eq__(self, other):
        return self.data == other.data

    def __mul__(self, other):
        result = make_matrix(self.N, other.L)
        for i in range(1, self.N+1):
            for j in range(1, other.L+1):
                for k in range(1, self.L+1):
                    result[i, j] += self[i, k] * other[k, j]
        return result

    def k0(self, i):
        return 1 if i <= self.L else i - self.L + 1

    def kN(self, i):
        return i + self.L - 1 if i <= self.N - self.L else self.N



