import string

print(string.printable)
p = string.printable
s1 = """Zfbi!tif!xpvme!qspcbcmz!fbu!nfA"""

s2 = """I love my kitty"""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for shift in range(len(SYMBOLS)):
    translated = ''
    for c in s1:
        if c in SYMBOLS:
            c_index = SYMBOLS.find(c)
            c_index -= shift
            if c_index < 0:
                c_index += len(SYMBOLS)
            translated += SYMBOLS[c_index]
        else:
            translated += c
    print(f"Shift: {shift}, {translated}")