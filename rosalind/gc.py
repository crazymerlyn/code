res = ""
m = 0.0

name = ""
dna = "T"

try:
    while True:
        string = raw_input().strip()

        if string and string[0] == '>':
            value = 1.0 * (dna.count("G") + dna.count("C")) / len(dna)
            if value > m:
                m = value
                res = name

            name = string[1:]
            dna = ""
        else:
            dna += string
except:
    pass

value = 1.0 * (dna.count("G") + dna.count("C")) / len(dna)
if value > m:
    m = value
    res = name

print res
print m*100

