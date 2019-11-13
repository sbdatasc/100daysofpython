from datetime import datetime
from datetime import date

#Exploring the datetime objects
today_date = datetime.today()
print("The Data type is : ", type(today_date))

#Exploring the attributes of a datetime object
print("Day: " , today_date.day)
print("Month : " , today_date.month)
print("Year: " , today_date.year)


