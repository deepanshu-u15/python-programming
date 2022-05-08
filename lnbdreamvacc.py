dictvacat={}
listvacat=[]
flistvacat=[]
fsetvacat={}
flist=[]
while True:
  poll=input("\nDo you want to join the poll ? (yes/no) :").upper()
  if poll=="YES":
    name=input("Enter the person name :")
    
    vacat=input("Enter the vacation place :")
    listvacat.append(vacat)
    while True:
      morevacat=input("Do you want vacation to be add ? (yes/no) :").upper()
      if morevacat=="YES":
        vacat=input("Enter the vacation place :")
        listvacat.append(vacat)

      elif morevacat=="NO":
        print(listvacat)
        dictvacat[name]=listvacat
        print(dictvacat)
        listvacat=[]
        break
  elif poll=="NO":
    break
  else:
    print("Invaid input !!!")
    break

for i in dictvacat:
  for j in range(len(dictvacat[i])):
    flistvacat.append(dictvacat[i][j])
    
fsetvacat=set(flistvacat)
print(f"The Dream Vacations place for all persons are :")
flist=list(fsetvacat)
for i in range(len(flist)):
  print(flist[i])