evenlist=[]
oddlist=[]
fdict={}
evenfilter=[]
oddfilter=[]
def even_filter(num):
  if num%2!=0:
    oddlist.append(num)
    return oddlist
def odd_filter(num):
  if num%2==0:
    evenlist.append(num)
    return evenlist
while True:

  q=input("\n Do you want to check the number (yes/no) :").upper()
  if q=="YES":
    num=int(input("Enter the number :"))
    even_filter(num)
    odd_filter(num)
    print(f"Even filter Output :{oddlist}")
    print(f"Odd filter Output :{evenlist}")

  else:
    break 
print(f"Even filter Output :{oddlist}")
print(f"Odd filter Output :{evenlist}")