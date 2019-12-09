
import copy

s = [[2,"ww"],3,"sssss"]

# s2 = s
s2 = s.copy()
s2 = copy.deepcopy(s)


s2[0][1] = "update"
s2[1] = "update"

print(s)
print(s2)