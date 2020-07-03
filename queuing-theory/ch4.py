# Simulation of an M/M/1

def exp_dist(x):
    """Returns an exponentially distributed random variable with mean 1/x."""
    from random import random
    from math import log
    return lambda : -log(1-random())/x

def sample(size_dist, arrival_dist):
    t = 0
    q = []
    for i in range(2001):
        t += arrival_dist()
        q.append((t, size_dist()))

    t = 0
    for arrival_time, size in q:
        t = max(t, arrival_time)
        t += size

    return t - q[-1][0]

def experiment(load_level):
    NUM_SAMPLE_RUNS = 200
    return sum(sample(exp_dist(1), exp_dist(load_level)) for _ in range(NUM_SAMPLE_RUNS)) / NUM_SAMPLE_RUNS

print([experiment(x) for x in [0.5, 0.7, 0.9]])

