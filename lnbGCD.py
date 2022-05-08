numlist=[]
gcdno=0
def gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcdno = i 
    return gcdno
listno=int(input("Enter the number of integer :"))
for i in range(listno):

  num1 =  int(input("Enter the number :"))
  numlist.append(num1)
for i in range(len(numlist)): 
  if i+1<len(numlist):
    gcdno=gcd(numlist[i], numlist[i+1])


print(f"The GCD of {numlist} is ", gcdno)