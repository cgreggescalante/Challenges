# Seven Wonders

l = input()

sc = [l.count("T"), l.count("C"), l.count("G")]

print(sc[0]**2 + sc[1]**2 + sc[2]**2 + min(sc) * 7)
