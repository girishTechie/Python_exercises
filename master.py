total = 10000
#effort = 3
effort = int(input("what is your daily effort? "))

days = total // effort
rem_hrs = total % effort
months = days // 30
days = days % 30 
years = months // 12 
months = months % 12

print(years, "YRS", months, "MNTHS", days, "DAYS", rem_hrs, "HRS")
