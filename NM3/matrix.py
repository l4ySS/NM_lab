from vector import *


def make_matrix(_N, _L):
    vectors = []
    for i in range(_N):
        vectors.append(make_vector(_L))
    return Matrix(vectors)


def make_diag(_N, y=None):
    vectors = []
    for i in range(_N):
        vectors.append(make_vector(_N))
    result = Matrix(vectors)
    if y is None:
        for i in range(1, _N + 1):
            result[i, i] = 1
    else:
        for i in range(1, _N+1):
            result[i, i] = y[i]
    return result


def make_e(_N):
    vectors = []
    for i in range(_N):
        vectors.append(make_vector(_N))
    result = Matrix(vectors)

    for i in range(1, _N + 1):
        result[i, i] = 1
    return result


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
        if isinstance(other, Matrix):
            result = make_matrix(self.N, other.L)
            for i in range(1, self.N+1):
                for j in range(1, other.L+1):
                    for k in range(1, self.L+1):
                        result[i, j] += self[i, k] * other[k, j]
            return result

        else:
            if isinstance(other, int):
                for i in range(1, self.N + 1):
                    for j in range(1, self.L + 1):
                        self[i, j] *= other
        return self

    def __copy__(self, other):
        for i in range(1, self.N + 1):
            for j in range(1, self.L + 1):
                self[i, j] = other[i, j]
        return self

    def transpose(self):
        result = make_matrix(self.L, self.N)
        for i in range(1, self.N+1):
            for j in range(1, self.L+1):
                result[j, i] = self[i, j]
        return result

    def find_max(self):
        [maxi, maxj] = [1, 2]
        for i in range(1, self.N):
            for j in range(i+1, self.L+1):
                if abs(self[i, j]) > abs(self[maxi, maxj]):
                    maxi = i
                    maxj = j
        return maxi, maxj

    def measure(self):
        t = 0
        for i in range(1, self.N):
            for j in range(i+1, self.L+1):
                if i != j:
                    t += 2*self[i, j]*self[i, j]
        return t

    def k0(self, i):
        return 1 if i <= self.L else i - self.L + 1

    def kN(self, i):
        return i + self.L - 1 if i <= self.N - self.L else self.N

    def norm(self):
        max = self[1, 1]
        for i in range(1, self.N+1):
            for j in range(i, self.L + 1):
                if abs(self[i, j]) > abs(max):
                    max = self[i, j]
        return abs(max)

