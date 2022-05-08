price=0
total=0
while True:

  age=int(input(f"Enter the age of person  :"))
  person=int(input(f"Total person :"))

  if age<3:
    price=0
  elif age>=3 and age<12:
    price=100
  else:
    price=150

  total=person*price
  
  print(f"Total Cost :Rs {total}")
  more=input(f"more data ? (y/n) :")
  if more=="n":
    break
  else:
    continue
