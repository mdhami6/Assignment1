#!/usr/bin/env python3
''' This program takes the date input from the user
    strips down any unsuable characters and returns
    a new sanitized output MMM DD, YYYY:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_mdhami6.py
Author: mdhami6
The python code in this file (a1_mdhami6.py) is original work written by
mdhami6. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import os
import sys




#Checks to see if the year is divisible by 4 and if it leaves a remainder more than one it is not a leap year
def leap_year(obj):
	if (obj % 4) >= 1:
		status = False
	else:
		status = True

	return status





#Takes user raw input and removes special characters and confirms if it is all digits
def sanitize(obj1):
	results = ""
	for character in obj1:
		if character.isalnum():
			results += character
	number = results.isdigit()
	if number == True:
		return results
	else:
		print("System error unknown characters used")
		sys.exit()


#Checks the length of the input to match with the date
def size_check(obj, intobj):
	if len(obj) == intobj:
		status = True
	else:
		status = False
	return status



#Checks input range for day, month and year to make sure it falls inside the range
def range_check(obj1, obj2):
	
	if int(obj1) in range(int(obj2[0]), (int(obj2[1])+ 1)):
		status = True
	else:
		status = False
	
	return status



#Returns how to use the program effectively if no arguments are entered
def usage():    
	status = "Usage: a1_mdhami6.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
	return status

if __name__ == "__main__":



   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()



   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]



   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data)
  # print('Sanitized user data:', dob)



   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()



   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])




   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()



   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)



   # step 8
   print(new_dob)  


