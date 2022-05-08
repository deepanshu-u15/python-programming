numblist=[]
factnumblist=[]
sumnumb=0
def fact(n):
  if (n==1 or n==0):
    return 1
  else:  
    return (n * fact(n - 1))

for i in range(5):
  numb=int(input(f"Enter the number {i+1} :"))
  if numb>=0:
    sumnumb+=numb
    numblist.append(numb)
    factnumb=fact(numb)
    factnumblist.append(factnumb)
  else:
    break
    
print(f"The number are :{numblist}")
print(f"The Sum of all numbers are :{sumnumb}")
print(f"The factorial of all number are :{factnumblist}")