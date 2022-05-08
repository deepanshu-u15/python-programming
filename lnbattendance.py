count=0
empno=int(input("Enter the number of Employees :"))
workday=int(input("Enter the number of Working days :"))
data=[]
if (empno<=10 and empno>=1)and(workday<=31 and workday>=1):
  for i in range(workday):
    attendata=input(f"Enter the Attendance details (P/A)  for day {i+1}:").upper()
    if len(attendata)==empno:
      data.append(attendata)  
    else:
      print(f"Invaid input!!!.\nEnter the number attendance like:-for all Present {'P'*empno} or for all Absent {'A'*empno}")
      break
  print(f"So the attendance data is :{data}")
  attend=0
  print("The maximum number of consecutive days on which all the employees are present on :")
  for attend in range(len(data)):

    if data[attend] =='P'*empno:
      count+=1
      print(attend+1)
else:
  print("Invaid input.. ")