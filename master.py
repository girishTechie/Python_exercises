total = 10000
#effort = 4
effort = int(input("what is your daily efffort? "))

days = total // effort
rem_hrs = total % effort
months = days // 30
rem_days = days % 30 
years = months // 12 
rem_months = months % 12

print(years, "YRS", rem_months, "MNTHS", rem_days, "DAYS", rem_hrs, "HRS")
