def lcm(x, y):
  if x > y:
    greater = x
  else:
    greater = y
  while(True):
    if((greater % x == 0) and (greater % y == 0)):
      lcm = greater
      break
    greater += 1
  return lcm
  
numblist=[]
for i in range(3): 
  numb=int(input(f"Enter the length of trek have travelled by friend {i+1} :"))
  numblist.append(numb)
print(f"The total length of trek they all have travelled :{lcm(lcm(numblist[0],numblist[1]),numblist[2])}")