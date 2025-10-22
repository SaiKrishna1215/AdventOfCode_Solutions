with open("input.txt") as f:
    s = f.read()

print(s.count("(") - s.count(")"))

pos = 0

for i in range(len(s)):
    if s[i] == "(":
        pos += 1
    else:
        pos -= 1
    
    if pos == -1:
        print(i)
        break