types = [0] * 8
types[0] = 1

leading_zeroes = 0

for _ in range(16):
    newtypes = [0 for _ in types]
    newtypes[0] = types[0] * 13
    newtypes[1] = types[0] + 14 * types[1]
    newtypes[2] = types[0] + 14 * types[2]
    newtypes[3] = types[0] + 14 * types[3]

    newtypes[4] = types[1] + types[2] + 15 * types[4]
    newtypes[5] = types[2] + types[3] + 15 * types[5]
    newtypes[6] = types[1] + types[3] + 15 * types[6]

    leading_zeroes += types[6]

    newtypes[7] = types[4] + types[5] + types[6] + 16 * types[7]

    types = newtypes

print hex(types[-1] - leading_zeroes).upper()

