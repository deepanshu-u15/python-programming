datalist=[]
databinlist=[]
databintuple=()

no=int(input("Enter the no of input (number should be (minimum10 & maximum 20):"))
if no>=10 and no<=20:
  for i in range(no):
    data=int(input(f"Enter the integer {i+1}:"))
    datalist.append(data)
    databin=int(bin(data).replace("0b", ""))
    databinlist.append(databin)
    finaland=databinlist[0]
    finaland=finaland & databinlist[i]
    finalor=databinlist[0]
    finalor=finalor | databinlist[i]
    databintuple=tuple(databinlist)

print(databintuple)
databinand=bin(finaland)
databinor=bin(finalor)
print(f"And of all input: {finaland}\nin binary format: {databinand},\n\nOr of all input: {finalor}\nin binary format: {databinor}")