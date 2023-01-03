v = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
n = int(input())
c=0
for i in range (n):
    s=input()
    c+=v.get(s,0)
print(c)
