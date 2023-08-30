line = sorted(map(int, input().split()))
tri = line[0] + line[1] + min(line[2], line[0]+line[1]-1)
print(tri)