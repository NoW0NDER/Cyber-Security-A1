ciphers ="""qeFIP?eGSeECNNS
5coOMXXcoPSZIWoQI
avnl1olyD4lylDohww6DhzDjhuDil
z.GM?.cEQc. 70c.7KcKMKHA9AGFK
?MFYp2pPJJUpZSIJWpRdpMFY
ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K
Zfbi!tif!xpvme!qspcbcmz!fbu!nfA"""

lines = ciphers.split("\n")
for i in range(len(lines)):
    with open("Q2_" + str(i) + ".txt", "w") as f:
        f.write(lines[i])

