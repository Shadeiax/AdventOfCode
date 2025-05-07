x = "Button A: X+94, Y+34"
print(x.split())
print(x.split()[2][1:-1])
a_x, a_y = map(int, x.split()[2][:1],x.split()[3][:1])

print(a_x, a_y)