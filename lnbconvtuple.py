datalis=[]
d1tuple=()
dataoutuple=()
datatup=()
dataoutlis=[]
dataouttup=()
lenum=int(input("Enter the number of input :"))
for i in range(lenum):
  num=int(input(f"Enter the data {i+1} :"))
  datalis.append(num)
d1tuple=tuple(datalis)
print(f"The tuple is : {d1tuple}")
strdata=input("Enter the string :")
for j in range(len(datalis)):
  if j/1==j:
    dataoutlis.append(datalis[j])
    dataoutlis.append(strdata)
dataoutuple=tuple(dataoutlis)
print(dataoutuple)