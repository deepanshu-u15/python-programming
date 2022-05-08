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