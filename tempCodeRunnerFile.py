numlist=[]
cubelist=[]
cubeno=0
cubesum=0
count=0
while True:
  q=input(f"\nDo you want to add a number to numlist {numlist} :(yes/no)").upper()
  if q=="YES":
    num=int(input("Enter the number : "))
    numlist.append(num)
    cube=lambda n:n*n*n
    for i in range(len(numlist)):
      cubeno=cube(numlist[i])
    cubelist.append(cubeno)
    print(numlist,cubelist)
    qsum=input(f"Do you need the sum of all cubic values? :(yes/no)").upper()
    if qsum=="YES":
      for i in range(len(cubelist)):
        cubesum+=cubelist[i]
      print(f"The sum of all cubic values is : {cubesum}")
    elif qsum=="NO":
      print(f"The cubic list is : {cubelist}")
    else:
      count+=1
      print(count)
      if count>3:
        break
      else:
        print(f"Reminder {count} :Input must be ‘yes’ or ‘no’! ")

  else:
    break