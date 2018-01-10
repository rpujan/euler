# 1 Jan 1900 was a Monday.
# 1900 was a leap year

# calculate start day of year 1901
start_day_of_1901 = 366 % 7 # 2 - tuesday
sum = 0

first_day_of_year = start_day_of_1901

for year in range(1901, 2001):
    days = 366 if ((year % 4 == 0) or (year % 400 == 0)) else 365       
    month_days = 0
    first_day_of_month = first_day_of_year
    for months in range(1,13):
        if months == 1 or months == 3 or months == 5 or months == 7 or months == 8 or months == 10 or months == 12:
            month_day = 31
        if months == 4 or months == 6 or months == 9 or months == 11:
            month_day = 30
        if months == 2:
            month_day = 28 if days == 365 else 29
        
        if first_day_of_month == 7:
            sum += 1
        
        first_day_of_next_month = (month_day % 7) + first_day_of_month
        first_day_of_month = first_day_of_next_month
        first_day_of_month = first_day_of_month if first_day_of_month <= 7 else first_day_of_month - 7
    
    start_day_of_next_year = (days % 7) + (first_day_of_year)
    start_day_of_next_year = start_day_of_next_year if start_day_of_next_year <=7 else start_day_of_next_year - 7
    first_day_of_year = start_day_of_next_year

print("Sundays fell on the first of the month from 1 Jan 1901 to 31 Dec 2000 : {}".format(sum))