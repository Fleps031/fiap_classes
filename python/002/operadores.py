import os
os.system('cls')

v1 = 10
v2 = 3

ans  = v1 + v2
print(ans)
ans = v1 - v2
print(ans)
ans = v1 * v2
print(ans)
ans = v1//v2
print(v1%v2)

print('par' if v1%v2 == 0 else 'impar')