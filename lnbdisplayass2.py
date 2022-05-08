numblist=[]
list1=[]
list2=[]
list3=[]
for i in range(100,501):
  if i%11==0 and not(i%2==0 or i%3==0):
    numblist.append(i)
print(numblist)
for i in range(len(numblist)):
  if i<2:
    list1.append(numblist[i])
  elif i>=2 and i<=5:
    list2.append(numblist[i])
  elif i>=6:
    list3.append(numblist[i])
print(f"Output :{list1},{list2},{list3}")
