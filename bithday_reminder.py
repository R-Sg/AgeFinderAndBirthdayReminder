import datetime  
from datetime import date 
  

def calculateAge(birthDate): 
  """
  function to  calculate age in years.
  """
  today = date.today() 
  age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  return age 

birthday_today = False
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')
bday_log = []

new = input('Add birthday in format yyyy-mm-dd:')
name = input('Whose bday?')
birthday_date = new.split( '-' )
current_age = calculateAge(date(int(birthday_date[0]), int(birthday_date[1]), int(birthday_date[2])))
print(name + " your age is {} years.".format(current_age))
bday_log.append((name, tuple(birthday_date)))

for birthday in bday_log:
   # current_dat[1] == birthday[1][1] this will check if current month is same as birth month  and current date is same as
   # birth date as per preadded log


   if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
       birthday_today = True
       age = int(current_date_lst[0]) - int(birthday[1][0])
       ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
       print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")

if not birthday_today:
  print(name + " today's not your birthday.")

