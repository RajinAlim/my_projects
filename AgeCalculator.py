import datetime
import sys

today = datetime.datetime.now()
try:
	if len(sys.argv) > 1:
		birth_txt = sys.argv[1]
	else:
		birth_txt = input("Enter your birthday in \'DD-MM-YYYY\' format:")
	birthday = datetime.datetime.strptime(birth_txt, "%d-%m-%Y")
	if birthday > today:
		raise Exception
except:
	print("\nInvalid Input!\nClosing Programme....")
	sys.exit()

if birthday == datetime.datetime(birthday.year, today.month, today.day):
	print("\nWow! It\'s your Birthday!\nWish You a Very Happy Birthday!")
print("\nYou were born on", birthday.strftime("%A, %d %B %Y"))
delta = today - birthday

total_days = delta.days
total_weeks = total_days // 7
total_months = total_days // 30
total_hours = (total_days * 24) + today.hour
total_minutes = (total_hours * 60) + today.minute

years = today.year - birthday.year
months = today.month - birthday.month
days = today.day - birthday.day
if days < 0:
	days = 30 + days
	months -= 1
if months < 0:
	months = 12 + months
	years -= 1

age = f"{years} years {months} months {days} days"
next_birthdate = datetime.datetime(today.year, birthday.month, birthday.day)
if next_birthdate < today:
	next_birthdate = datetime.datetime(today.year + 1, birthday.month, birthday.day)
next_bd_after = (next_birthdate - today).days + 1
next_birthday = "Tomorrow!" if next_bd_after == 1 else "after " + str(next_bd_after) + " days"

nextm = lambda d : ((total_days // d) + 1) * d
previous = lambda d : ((total_days // d) - 1) * d
m = [100, 1000, nextm(100)]

if total_days < 1000:
	m.extend([250, 500, previous(250), nextm(2500)])
if total_days > 1000 and total_days <= 20000:
	m.extend([500, 5000, 7500, 10000, nextm(500), previous(1000), nextm(1000)])
if total_days > 20000 and total_days <= 50000:
	m.extend([5000, 10000, 25000, nextm(2500), previous(1000), nextm(1000)])
if total_days > 50000:
	m.extend([5000, 1000, 25000, 50000, previous(5000), nextm(5000), nextm(1000)])
m = sorted(list(set(m)))

milestones = {"past": [], "soon": [], "future": []}
for ms in m:
	date = birthday + datetime.timedelta(days=ms)
	difference = (date - today).days
	if difference > 0 and difference < 365:
		milestones['soon'].append((ms, date.strftime("%A, %d %B %Y")))
	elif date < today:
		milestones['past'].append((ms, date.strftime("%A, %d %B %Y")))
	elif date > today:
		milestones['future'].append((ms, date.strftime("%A, %d %B %Y")))

print("\nYour Age is", age)
print("\nHere is some details about age:")
print("Total Months:", total_months)
print("Total Weeks:", total_weeks)
print("Total Days:", total_days)
print("Total Hours:", total_hours)
print("Total Minutes:", total_minutes)
print("\nYour next birthday-{0} is {1}".format(next_birthdate.strftime("%A, %d-%B-%Y"), next_birthday))

print("\nYou had completed-\n")
for ms in milestones['past']:
	print("  Your {0} days on {1}".format(ms[0], ms[1]))
if milestones['soon']:
	print("\nYou are complete-\n")
	for ms in milestones['soon']:
		print("  Your {0} days on {1}".format(ms[0], ms[1]))
print("\nYou will complete-\n")
for ms in milestones['future']:
	print("  Your {0} days on {1}".format(ms[0], ms[1]))

print("""\n\n
Project: Age Calculator
Version: 2.5
Author: Rajin Alim
Completed On Wednesday, 1 July 2020""")
