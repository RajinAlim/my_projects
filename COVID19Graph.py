#requried Third Party Modules are matplotlib and requests.

import datetime
import math
import requests
import sys
from itertools import chain
from matplotlib import pyplot
from matplotlib import dates as dt


def pretify_number(n):
    asstring = list(str(n))
    asstring.reverse()
    for i in range(len(asstring)):
        if (i + 1) % 3 == 0 and i < len(asstring) - 1:
            asstring[i] = "," + asstring[i]
    return ''.join(asstring[::-1])

country = input("Enter Country: ").strip().title()
req_url = "https://api.covid19api.com/dayone/country/{}".format(country.replace(' ', '-').lower())
try:
    res = requests.get(req_url)
    res.raise_for_status()
    records = res.json()
except Exception as exc:
    print("Failed to collect statistics.\nPossible reason: no internet connection or invalid connection from server.")
    print("\nError message:", exc)
    sys.exit()

data = [[0]  for _ in range(6)]
total_cases, total_recovered, active, total_deaths, cases, deaths = data
labels = "Total Cases", "Total Recovered", "Active Cases", "Total Deaths", "Cases Per Day", "Deaths Per Day"
plots = ((0, 1, 2), (3, 4), (5, ))
dates = []
for record in records:
    total_cases.append(record['Confirmed'])
    total_deaths.append(record['Deaths'])
    total_recovered.append(record['Recovered'])
    active.append(record['Active'])
    dates.append(datetime.datetime.strptime(record['Date'][:10], "%Y-%m-%d"))
    cases.append(total_cases[-1] - total_cases[-2])
    deaths.append(total_deaths[-1] - total_deaths[-2])
prev_day = dates[0] - datetime.timedelta(days=1)
dates.insert(0, prev_day)

y_maxes = [0] * len(plots)
for i, plot in enumerate(plots):
    y_max = max(chain.from_iterable([data[i] for i in plot]))
    ex = int(math.log(y_max, 10))
    coefficient = math.ceil(y_max / (10 ** ex))
    y_max = coefficient * (10 ** ex)
    y_maxes[i] = y_max

pyplot.style.use(pyplot.style.available[2])
fig, axes = pyplot.subplots(len(plots), sharex=True)
fig.suptitle("COVID-19 Statistics Graph of " + country, fontsize=10)
for axis, plot, ymax in zip(axes, plots, y_maxes):
    axis.set_xlabel("Dates", fontsize=8)
    axis.set_ylabel("Statistics", fontsize=8)
    x_tick_count = 7
    y_tick_count = 5
    axis.axis([dates[0], dates[-1], 0, ymax])
    fig.autofmt_xdate(rotation=60)
    axis.xaxis.set_major_formatter(dt.DateFormatter("%d-%m-%Y"))
    x_ticks = [dates[i * (len(dates) // x_tick_count)] for i in range(x_tick_count + 1)]
    axis.set_xticks(ticks=x_ticks)
    yticks = [i * (ymax // y_tick_count) for i in range(y_tick_count + 1)]
    axis.set_yticks(yticks)
    axis.set_yticklabels(list(map(lambda tick: pretify_number(tick), yticks)))
    axis.tick_params(labelsize=7.5)
    for j in plot:
        axis.plot_date(dates, data[j], label=labels[j], marker=None, linestyle="-", linewidth=1)
    axis.legend(loc="upper left", fontsize=6)

pyplot.show()


"""Project: COVID19 Statistics Graph
Author: Rajin Alim
Completed On Sunday, 14 March 2021 02:18 PM"""
