import time

print("Enter To Start,\nEnter for Lap,\nCTRL+C to stop")
def as_str(time):
	milis = int(str(time).split('.')[1])
	sec = int(str(time).split('.')[0])
	minutes = sec // 60
	sec %= 60
	return '{0}:{1}:{2}'.format(minutes, sec, milis)

input()
print('Started')
start_time = round(time.time(), 2)
end_time = None
lap_count = 1

try:
	while True:
		input()
		lap = round(time.time() - start_time, 2)
		print('Lap', str(lap_count) + ',', as_str(lap))
		lap_count += 1

except KeyboardInterrupt:
	end_time = round(time.time() - start_time, 2)
	print('End:', as_str(end_time))