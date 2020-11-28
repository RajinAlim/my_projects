import sys
import re
import html
import requests

base_url = "http://quotes.toscrape.com"
count = 0
if len(sys.argv) > 1:
	if sys.argv[1].isnumeric():
		count = int(sys.argv[1])
	else:
		tag = sys.argv[1]
		base_url = base_url + "/tag/" + tag.strip().lower()
		if len(sys.argv) == 3:
			count = int(sys.argv[2])
res = requests.get(base_url)
res.raise_for_status()

quote_pat = r"<span class=\"text\" itemprop=\"text\">(.+?)</span>\s*?.+?class=\"author\".+?>(.+?)</small>"
next_pat = r"<a href=\"(.+?)\">Next"
quotes = re.findall(quote_pat, res.text)
if len(quotes) < count:
	match = re.search(next_pat, res.text)
	while len(quotes) < count and match:
		next_page = "http://quotes.toscrape.com/" + match.group(1)
		r = requests.get(next_page)
		quotes = quotes + re.findall(quote_pat, r.text)
		current_page = next_page
		current_res = requests.get(current_page)
		match = re.search(next_pat, current_res.text)

if count and len(quotes) > count:
	quotes = quotes[:count]
for quote in quotes:
	print(f"{html.unescape(quote[0])}\n-{html.unescape(quote[1])}\n")