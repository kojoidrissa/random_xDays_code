f = open("scores.txt", "r")

students ={}

for line in f:
    entry = line.strip().split(",")