se = input()
s = list(se)
max = 0
spel = [0] * 26
for i in range(len(s)):
    s[i] = s[i].lower()
    spel[ord(s[i]) - 97] += 1
for i in range(26):
    if int(spel[i]) > int(max):
        max = spel[i]
    elif int(spel[i]) == int(max):
        max = 0
if max == 0:
    print("?")
else:
    print(chr(spel.index(max) + 65))
