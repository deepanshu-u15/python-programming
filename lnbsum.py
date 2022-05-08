intlist=[]
sum=0
for i in range(5):
  no=int(input(f"Enter number {i+1}  :"))
  if no >=9:
    sum+=no
    intlist.append(no)
print(f"The sum of {intlist} is :{sum}")