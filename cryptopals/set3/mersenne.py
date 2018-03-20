class Mersenne(object):
    def __init__(self, seed=None):
        if seed is None:
            import time
            seed = int(time.time())
        self.N = 624
        self.M = 397

        self.matrix_a   = 0x9908b0df
        self.upper_mask = 0x80000000
        self.lower_mask = 0x7fffffff

        self.mt = [0] * self.N
        self.mti = self.N + 1

        self.init_genrand(seed)

    def init_genrand(self, seed):
        self.mt[0] = seed
        for i in range(1, self.N):
            self.mti = i
            s = self.mt[i-1] ^ (self.mt[i-1] >> 30)
            self.mt[i] = ((((s & 0xffff0000) >> 16) * 1812433253) << 16) + (s & 0x0000ffff) * 1812433253 + self.mti
            self.mt[i] >>= 0



