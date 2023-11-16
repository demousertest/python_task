receptor = {'A' : 'a',
           'B' : '0',
           'C' : '1',
           'D' : '2'}

opp_sides = {
    'a' : "BC",
    "b" : "CD",
    "c" : "DA",
    "d" : "AB"
}

distance = {
    "BC" : '0-1',
    "CD" : '1-2',
    "DA" : '2-a',
    "AB" : 'a-0'
}

mirror_receptor = ""
for k, v in receptor.items():
    if v.isalpha():
        if v == 'a':
            opposite_side = opp_sides[v]
            mirror_receptor += 'D'
        elif v == 'b':
            opposite_side = opp_sides[v]
            mirror_receptor += 'A'
        elif v == 'c':
            opposite_side = opp_sides[v]
            mirror_receptor += 'B'
        elif v == 'd':
            opposite_side = opp_sides[v]
            mirror_receptor += 'C'

print(f"opposite side : {opposite_side}")
print(f"Ray meet receptor {receptor[mirror_receptor]}")


# """
# AB = 
# B = 0
# C = 1
# D = 2
# A = a
# a = 0-1
# a = D
# a <-> BC
# b <-> CD
# c <-> DA
# d <-> AB
# BC = 0-1
# CD = 1-2

# """