string = """A Y
B X
C Z"""

"""
A - 1 Rock
B - 2 Paper
C - 3 Scissors

X - 0 Lose 
Y - 3 Draw
Z - 6 Win
"""




a = string.split("\n")
b = []
for pair in a:
    b.append(pair.split(" "))
print(b)
#ureditev seznama


score = 0
for pair in b:
    if pair[1] == "X":
        score += 1
        if pair[0] ==  "A":
            score += 3
        if pair[0] ==  "B":
            score += 0
        if pair[0] ==  "C":
            score += 6
    elif pair[1] == "Y":
        score += 2
        if pair[0] ==  "A":
            score += 6
        if pair[0] ==  "B":
            score += 3
        if pair[0] ==  "C":
            score += 0
    elif pair[1] == "Z":
        score += 3
        if pair[0] ==  "A":
            score += 0
        if pair[0] ==  "B":
            score += 6
        if pair[0] ==  "C":
            score += 3



print(score)