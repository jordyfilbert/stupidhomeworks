inp=0
result=0
list1=[]

for i in range(10):
    inp=int(input())
    list1.append(inp%42)

# print (list1)
var = set(list1)
# print (var)
res = len(var)
print(res)
