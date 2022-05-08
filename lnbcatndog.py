catcount=0
dogcount=0
inputstr=input("Enter the string :")
catcount=inputstr.count('cat')
dogcount=inputstr.count('dog')
if catcount==dogcount:
  print("The result is : True")
else:
  print("The result is : False")
