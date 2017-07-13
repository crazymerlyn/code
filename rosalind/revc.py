match = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}

print "".join(match[b] for b in reversed(raw_input().strip()))
