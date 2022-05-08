plist=[]

para=input("Enter the string :")
p=para.split(" ")

for i in range(len(p)):
  p[i] =  ''.join(filter(str.isalnum, p[i])) 
  if len(p[i])>4:
    plist.append(p[i])
print(plist)