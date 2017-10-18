temp=0
arr=[1,0,0]
inp=input()

for i in inp:

    if i.upper()=="A":
        temp = arr[1]
        arr[1] = arr[0]
        arr[0] = temp

    elif i.upper()=="B":
        temp = arr[2]
        arr[2] = arr[1]
        arr[1] = temp

    elif i.upper()=="C":
        temp = arr[2]
        arr[2] = arr[0]
        arr[0] = temp

# print (arr)


if arr[0]==1:
    print  ("1")
elif arr[1]==1:
    print ("2")
elif arr[2]==1:
    print ("3")
