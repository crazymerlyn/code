LIMIT = 10**9
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
nums = [1]
for p in primes:
    new = []
    for v in nums:
        while v <= LIMIT:
            new.append(v)
            v *= p
    nums = new
print(len(nums))
