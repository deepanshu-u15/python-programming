n=input("Enter a string :")
print("length of string is:",+(len(n)))

if  len(n)<=7:
    print(n[1:len(n):2])
elif len(n)>7:
    print(n[0:len(n):2])