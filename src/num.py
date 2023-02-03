import math
from utils import rnd


class Num:

    def __init__(self, txt=None, at=None):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf')
        self.hi = float('-inf')

        if at:
            self.at = at
        else:
            self.at = 0

        if txt:
            self.txt = txt
            if self.txt[-1] == '-':
                self.w = -1
            else:
                self.w = 1
        else:
            self.txt = ""

    def add(self, n):
        '''
        Addition method for n
        '''
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        '''
        Method for calculating mean
        '''
        return self.mu

    def div(self):
        '''
        Method for calculating Standard Deviation
        '''
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5

    def rnd(self, x, n) -> float:
        '''
        Helper method
        '''
        if x == '?':
            return x
        else:
            return rnd(x, n)

    def norm(self, n):
        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)


    def dist(self, n1, n2):

        if n1 == "?" and n2 == "?":
            return 1
        n1 = self.norm(n1)
        n2 = self.norm(n2)
        if n1 == "?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0
        if n2 == "?":
            if n1 < 0.5:
                n2 = 1
            else:
                n2 = 0

        return abs(n1 - n2)