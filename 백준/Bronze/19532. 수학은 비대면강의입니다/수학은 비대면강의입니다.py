a, b, c, d, e, f = map(int, input().split())

#ax+by=c
#dx+ey=f
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)