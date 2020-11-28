import requests
from operator import itemgetter
import sys

def present_report(report):
	if report['country'] == "World":
		print('\nWorld\' Report:')
	else:
		print('\nCountry:', report['country'])
	print('Total Cases In Last 24 Hours:', report['todayCases'])
	print('Total Deaths In Last 24 Hours:', report['todayDeaths'])
	print('Total Cases:', report['cases'])
	print('Total Deaths:', report['deaths'])
	if report.get('deathRate'):
		print('Death Rate:', str(report['deathRate']) + '%')
	print('Recovered:', report['recovered'])
	if report.get('recoveryRate'):
		print('Recovery Rate:', str(report['recoveryRate']) + '%')
	active_rate = round(100 - (report.get('deathRate') + report.get('recoveryRate')), 2)
	print('Active/Infected Patients At Present: ', str(report['active']) + '(' + str(active_rate) + '%)')
	print('Critical:', report['critical'])
	print('Casses Per Million:', report['casesPerOneMillion'])
	print('Deaths Per Million:', report['deathsPerOneMillion'])

def present_ranked_report(report):
	ranked_report = sorted(report, key=itemgetter('todayCases'), reverse=True)[0]
	print('\nMost Cases In Last 24 Hours In', ranked_report['country'], ',', ranked_report['todayCases'])
	ranked_report = sorted(report, key=itemgetter('todayDeaths'), reverse=True)[0]
	print('Most Deaths In Last 24 Hours In', ranked_report['country'], ',', ranked_report['todayDeaths'])
	ranked_report = sorted(report, key=itemgetter('cases'), reverse=True)[0]
	print('Most Cases In', ranked_report['country'], ',', ranked_report['cases'])
	ranked_report = sorted(report, key=itemgetter('deaths'), reverse=True)[0]
	print('Most Deaths In', ranked_report['country'], ',', ranked_report['deaths'])
	try:
		ranked_report = sorted(report, key=itemgetter('deathRate'), reverse=True)[0]
		print('Most Death Rate In', ranked_report['country'], ',', str(ranked_report['deathRate']) + '%')
	except:
		pass
	ranked_report = sorted(report, key=itemgetter('casesPerOneMillion'), reverse=True)[0]
	print('Most Cases Per Million In', ranked_report['country'], ',', ranked_report['casesPerOneMillion'])
	ranked_report = sorted(report, key=itemgetter('deathsPerOneMillion'), reverse=True)[0]
	print('Most Deaths Per Million In', ranked_report['country'], ',', ranked_report['deathsPerOneMillion'])

try:
	url = 'https://coronavirus-19-api.herokuapp.com/countries'
	reader = requests.get(url)
	reader.raise_for_status()
except Exception as exp:
	print("Error", exp)

data_store = reader.json()
country_data = {}
country_rank = None

if len(sys.argv) > 1:
	home_country = sys.argv[1].lower().strip()
else:
	home_country = input("Enter Your Country: ").lower().strip()

for data in data_store:
	try:
		recovery_rate = round((int(data['recovered']) / int(data['cases'])) * 100, 2)
		data['recoveryRate'] = recovery_rate
	except:
		data['recoveryRate'] = 0
	try:
		death_rate = round((int(data['deaths']) / int(data['cases'])) * 100, 2)
		data['deathRate'] = death_rate
	except:
		data['deathRate'] = 0
	if data['country'].lower() == home_country:
		country_data = data
		country_rank = data_store.index(data)

if country_data:
	print('\nReport of Your Country,', home_country.title(), ':')
	present_report(country_data)
	print('Rank: ', country_rank)

world_report = data_store[0]
data_store.remove(world_report)
data_store.remove(country_data)

present_report(world_report)
present_ranked_report(data_store)

print('\n\nNews of 10 other countries with most serious condition:')

for data in data_store[:10]:
	present_report(data)

print("\n\n[Source: https://coronavirus-19-api.herokuapp.com]")