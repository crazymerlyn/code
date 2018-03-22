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

    def genrand_int32(self):
        mag01 = [0, self.matrix_a]
        if self.mti >= self.N:
            if self.mti == self.N + 1:
                self.init_genrand(5489)

            for k in range(self.N - self.M):
                y = (self.mt[k] & self.upper_mask) | (self.mt[k+1] & self.lower_mask)
                self.mt[k] = self.mt[k + self.M] ^ (y >> 1) ^ mag01[y & 1]

            for k in range(self.N - self.M, self.N - 1):
                y = (self.mt[k] & self.upper_mask) | (self.mt[k+1] & self.lower_mask)
                self.mt[k] = self.mt[k + self.M - self.N] ^ (y >> 1) ^ mag01[y & 1]

            y = (self.mt[self.N - 1] & self.upper_mask) | (self.mt[0] & self.lower_mask)
            self.mt[self.N - 1] = self.mt[self.M - 1] ^ (y >> 1) ^ mag01[y & 1]
            for i in range(len(self.mt)):
                self.mt[i] &= 0xffffffff
            self.mti = 0
        y = self.mt[self.mti]
        self.mti += 1
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)

        return y



if __name__ == '__main__':
    a = Mersenne()
    n = 10 ** 5
    count = 0
    for _ in range(n):
        x = a.genrand_int32() / 2.0 ** 32
        y = a.genrand_int32() / 2.0 ** 32
        if x ** 2 + y ** 2 <= 1:
            count += 1
    print(4.0 * count/n)

