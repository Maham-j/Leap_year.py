def is_leap_year(year):
    leap = False
    if year % 4 ==0 and (year % 100 !=0 or year % 400 ==0):         # If year is divisible by 4 and not by 100, or divisible by 400
        leap = True
    return leap
year = int (input('Enter year: '))    # Get input year from user
print (is_leap_year (year))
    
