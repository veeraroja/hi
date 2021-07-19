#program on age
from datetime import date
DOB = input('please tell me your date of year')
DOBValue = int (DOB)
presentYear = date.today().year
age = presentYear - DOBValue
print ('your age is', age, sep="->")

