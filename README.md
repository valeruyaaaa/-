a,b = map(int, input('a,b (a > b): ').split())
print(*list(range(a-1+a%2, b-1, -2)))
