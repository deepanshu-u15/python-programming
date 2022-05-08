lis=[]
lis2=[]
lis2sq=[]
lis3=[]
lis4=[]
lis5=[]

for i in range(20):
  datalis=int(input(f"Enter the integer {i+1} :"))
  lis.append(datalis)
  if i==0 or i==15 or i==16 or i==17 or i==18 or i==19 :
    lis2.append(lis[i])

for j in range(len(lis2)):
  datasq=lis2[j]**2
  lis2sq.append(datasq)

print(f"list 1 :{lis}")
print(f"list 2 :{lis2}")
print(f"list 3 :{lis2sq}")

for k in range(len(lis2sq)):
  if k<=2:
    lis3.append(lis2sq[k])
  elif k==3:
    lis4.append(lis2sq[k])
  elif k==5 or k==4:
    lis5.append(lis2sq[k])

print(f"list 4 :{lis3}")
print(f"list 5 :{lis4}")
print(f"list 6 :{lis5}")
