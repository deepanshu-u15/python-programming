namelist=[]
marklist=[]
studict={}
studno=int(input("\nEnter the number of student :"))
for i in range(studno):
  name=input(f"Enter the name of student {i+1} :")
  mark=int(input(f"Enter the mark of studend {i+1} :"))
  namelist.append(name)
  marklist.append(mark)
  studict[name]=mark
print(f"Name of the student :{namelist}")
print(f"Mark of the student :{marklist}")
print(f"Detail of the student :{studict}")
