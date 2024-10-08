# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

# 28

# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
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
    
def days_in_month(year, month):
  #list of days in each month
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  #catch if input is not within range
  if month > 12 or month < 1:
    return "Invalid month"
  #check if it is a leap year and we are looking for february
  if is_leap(year) and month == 2:
    return 29
  #else look up days and return accordingly
  return month_days[month -1]


  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

days = days_in_month(year, month)
print(days)
