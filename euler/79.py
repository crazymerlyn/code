def scs(strings):
    res = []

    while strings:
        not_first = []
        first = []
        for s in strings:
            first.append(s[0])
            for c in s[1:]:
                not_first.append(c)

        chosen = None
        for digit in first:
            if digit not in not_first:
                chosen = digit
                break

        assert chosen is not None
        res.append(chosen)

        newstrings = []
        for s in strings:
            if s[0] == chosen:
                if s[1:]:
                    newstrings.append(s[1:])
            else:
                newstrings.append(s)
        strings = newstrings

    return "".join(res)

with open("keylog.txt") as f:
    lines = [l.strip() for l in f.readlines()]

    print scs(lines)
