words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def letter_count(n):
    if n == 1000:
        return len("onethousand")
    s = ""
    if n >= 100:
        s += words[n // 100] + "hundred"
        if n % 100 != 0:
            s += "and"
        n %= 100
    if n >= 20:
        s += tens[n // 10]
        n %= 10
    if n > 0:
        s += words[n]
    return len(s)

print(sum(letter_count(i) for i in range(1, 1001)))
