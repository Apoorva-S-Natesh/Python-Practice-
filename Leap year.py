#this program was created with a focus on defining functions and calling functions by working with giving arguments to the parameters and returning values
def is_leap(year):
  #if a year is divisible by 4 and 100 then it has to be divisible by 400 in order to be a leap year.
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year,month):
    if month>12 or month< 1:
        return "invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month==2:
        return 29
    return month_days[month -1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
