result=0
num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
operation=int(input("Select which operation you want to perform\nAdd -- 1\nSub -- 2\nMultiply -- 3\nDivide -- 4:\n"))

if operation==1:
  print(f"Add :{num1+num2}")

elif operation==2:
  print(f"Sub :{num1-num2}")

elif operation==3:
  print(f"Multiply :{num1*num2}")

elif operation==4:
  if num2!=0:
    print(f"Divide :{num1/num2}")
  else:
    print("can't divide by 0")

else:
  print("Invalid Input...Try again")