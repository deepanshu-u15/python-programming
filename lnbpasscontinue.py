listnumb=[]

no=int(input("total number of input :"))
for i in range(no):
  binumb=input(f"binary number :") 
  numb=int(binumb,2)
  print(binumb,numb)
  listnumb.append(numb)
min=listnumb[0]
max=listnumb[0]
for i in range(len(listnumb)):
  if min>listnumb[i]:
    min=listnumb[i]
  if max<listnumb[i]:
    max=listnumb[i]
  if listnumb[i]%5!=0:
    print(listnumb[i])
    break
  else:
    print(listnumb[i])

print(min,max)