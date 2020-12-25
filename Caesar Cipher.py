a = input()
d = int(input())
trans = ""
for i in a:
    b = ord(i) + d
    if b > 122:
        b = (b-122) + 96
        trans = trans + chr(b)
    else:
        trans = trans + chr(b)
print(trans)