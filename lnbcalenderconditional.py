import calendar
year=int(input("Enter the year :"))
month=int(input("Enter the month :"))
day=int(input("Enter the day :"))
print(calendar.month(year, month))
if year%4==0:
  print(f"The number of days in {year} is 366")
else:
  ly=year%4 #2017 1,2018 2,2019 3,2020 0
  year=year-ly+4
  print(f"The next Leap year is :{year}")