mylist=[233, 6.66, "hhh", ["x1", "x2"]]
for item in mylist:
    print(item, end=' ')
print()

evennumbers= list(range(2, 11, 2))
print(evennumbers, end=" ")
print("sum="+str(sum(evennumbers)), end=" "); print("max="+str(max(evennumbers)))

squares=[]
for num in range(1, 11):
    squares.append(num**2)
print(squares[-3:])
squares.clear()
squares=[num**2 for num in range(1, 11)]
for i in range(len(squares)):
    print(squares[i], end=" ")
print()

print(list(range(0, 13, 3)))

currentnum=1
while currentnum<=5:
    print(currentnum, end=" ")
    currentnum+=1
print()

print("Enter a number, 0 to quit ")
while True:
    xin=int(input())
    if xin==0:
        break
    elif xin!=1:
        print("You inputed: "+str(xin))

list1=[1, 2, 3]
list2=[]
for x in list1: # x=1, then x=3, no x=2
    list2.append(x)
    del list1[0]  # do not change list inside for-each, will cause iterator error
print(list1, list2)
