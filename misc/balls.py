from random import uniform

def simulate(power):
    def next_bin(a, b):
        s = a ** power + b ** power
        if uniform(0, s) <= a ** power:
            return 0
        else:
            return 1

    bins = [1, 1]
    for _ in range(1000):
        bins[next_bin(*bins)] += 1
        print(bins)


if __name__ == '__main__':
    simulate(1.8)
