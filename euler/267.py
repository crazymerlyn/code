from math import log, ceil
from utils import comb


last = 0
guess = 0.5
stepsize = 1e-6

def n_successes(guess):
    return (9 - log(1- guess, 10) * 1000) / (log(1 + 2 * guess, 10) - log(1 - guess, 10))

def fdiff(guess):
    e = 1e-6
    return (n_successes(guess + e) - n_successes(guess)) / e

while abs(last - guess) > 1e-12:
    last = guess
    guess -= fdiff(guess) * stepsize

successes = int(ceil(n_successes(guess)))

res = 0
for i in range(successes, 1001):
    res += comb(1000, i)

print "%.12f" % (res / 2.0 ** 1000)

