count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                S = a + b + c + d
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            h = S - e - f - g
                            if not (0 <= h <= 9):
                                continue
                            for i in range(10):
                                j = a + e + i - d - g
                                if not (0 <= j <= 9):
                                    continue
                                k = b + c + 2 * d - e - f - i
                                if not (0 <= k <= 9):
                                    continue
                                l = f + g - i
                                if not (0 <= l <= 9):
                                    continue
                                m = b + c + d - e - i
                                if not (0 <= m <= 9):
                                    continue
                                n = c + 2 * d - f - e - i + g
                                if not (0 <= n <= 9):
                                    continue
                                o = a - c - d + e + f + i - g
                                if not (0 <= o <= 9):
                                    continue
                                p = e + i - d
                                if not (0 <= p <= 9):
                                    continue
                                count += 1
print(count)
