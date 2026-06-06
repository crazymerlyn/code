# 1_2_3_4_5_6_7_8_9_0
# Last digit is 0, so n ends in 0 → n^2 ends in 00
# So the pattern is 1_2_3_4_5_6_7_8_9_00
# n = 10 * m, so n^2 = 100 * m^2, and m^2 = 1_2_3_4_5_6_7_8_9
# m is in range sqrt(10203040506070809) to sqrt(19293949596979899)
# ≈ 101010101 to 138902662
# m must end in 3 or 7 (for square to end in 9)
# Also the hundreds digit of m^2 is 8 → the last two digits of m are:
# m mod 100 → m^2 mod 1000 pattern. Since m^2 = ..._8_9 ≡ 89 mod 100, 
# m ends in 33, 67, 83, or 17 (since 33^2=1089, 67^2=4489, 83^2=6889, 17^2=289)
# Wait, 289 ≡ 89 mod 100 but 289 has hundreds digit 2, not 8.
# Let me just check which m give _89 as last two digits:
# m^2 ≡ 89 mod 100 → m ≡ 17, 33, 67, 83 (mod 100)
# The hundreds digit of m^2 should be 8.
# Let's check: 33^2=1089 → 089 → 0 hundreds digit. 67^2=4489 → 489 → 4. 83^2=6889 → 889 → 8. 17^2=289 → 289 → 2.
# So only m ≡ 83 (mod 100) gives hundreds digit 8.

for m in range(101010101, 138902663, 10):
    if m % 10 not in (3, 7):
        continue
    s = str(m * m)
    if len(s) != 17:
        continue
    if all(s[2*i] == str(i+1) for i in range(9)):
        print(m * 10)
        break
