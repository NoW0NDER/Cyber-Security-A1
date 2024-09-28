def charDiff(s):
    return (ord(s[0]) - ord(s[1]))%26

print(charDiff("Iq"))
print(charDiff("gt"))