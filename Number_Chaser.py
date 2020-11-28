from re import search
import datetime
import math

class MyMaths:
	
	@staticmethod
	def present_features():
		print("Check out the available features:\n1.Get factors of a number.\n2.Get prime factors of a number\n3.Check if a number is Prime Number or not.\n4.Check if a number is Fibonacci Number or not.\n5.Get nearest Prime number of a number.\n6.Get nearest Fibonacci number of a number\n7.Find all Prime Numbers within a range.\n8.Find all Fibonacci Numbers within a range.\n9.Get nth Fibonacci Number.\n10.Calculate GCD of multiple numbers.\n11.Calculate LCM of multiple numbers.\n12.Check if a number is Square Number or not.\n13.Check if a number is Cube Number or not.\n14.Get nearest Square number of a number.\n15.Get nearest Cube number of a number.\n16.Get all Square numbers within a range.\n17.Get all Cube numbers within a range.\n18.Express a numbers as Sum of two squares.\n19.Express a number as Substraction of two squares.\n20.Express a number as Sum of two cubes.\n21.Express a number as Substraction of two cubes.\n22.Find all numbers that can be expressed as Sum of two squares within a range.\n23.Find all numbers that can be expressed as Substraction of two squares within a range.\n24.Find all numbers that can be expressed as Sum of two cubes within a range.\n25.Find all numbers that can be expressed as Substraction of two cubes\n26.Search numbers with specific conditions")
	
	@staticmethod
	def perform():
		MyMaths.present_features()
		topics = ["Factors", "Prime Factors", "Prime", "Fibonacci", "Prime", "Fibonacci", "Prime", "Fibonacci", "GCD", "LCM", "Square", "Cube", "Square", "Cube", "Square", "Cube", "Sum of two squares", "Substraction of two squares", "Sum of two cubes", "Substraction of two cubes", "Sum of two squares", "Substraction of two squares", "Sum of two cubes", "Substraction of two cubes"]
		task = int(input("\nEnter the number of the activity you want to perform:"))
		def checker(func):
			try:
				n = int(input("\nEnter a number:"))
			except ValueError:
				print("Invalid Input")
				MyMaths.perform()
			res = func(n)
			if res:
				print("\n{0} is a {1} number".format(n, topics[task - 1]))
			else:
				print("\n{0} is not a {1} number".format(n, topics[task - 1]))
		
		def finder_1(func):
			i = str(input("\nEnter the range/ min & max value.\n(Put a comma(,) between the values)\n\nrange(min, max):"))
			input_pattern = r"(\d+)[\D\W]+(\d+)"
			analyzer = search(input_pattern, i)
			try:
				assert not analyzer
				min, max = int(analyzer.group(1)), int(analyzer.group(2))
			except:
				print("Invalid Input")
				MyMaths.perform()
			results = list(func(min, max))
			print("\nBetween {0} and {1}, there are {2} {3} numbers.\nThey are:\n{4}".format(min, max, len(results), topics[task - 1], presentation(results)))
		
		def nearest(func):
			try:
				n = int(input("\nEnter a number:"))
			except ValueError:
				print("Invalid Input")
				MyMaths.perform()
			for i in range(n):
				k = n + i
				if k < 2147483647 and func(k):
					res = k
					break
				k = n - i
				if k > 0 and func(k):
					res = k
					break
			print("\nNearest {0} number of {1} is {2}".format(topics[task - 1], n, res))
		
		def calculator(func):
			l = str(input("\nEnter the numbers,put a comma(,) between two numbers\nNumbers:")).split(",")
			nums = []
			for n in l:
				try:
					nums.append(int(n))
				except ValueError:
					break
					print("Invalid Input")
					MyMaths.perform()
			result = func(*nums)
			print("\n{0} of {1} is {2}".format(topics[task - 1], presentation(nums), result))
		
		def expressor(func):
			n = int(input("\nEnter the number:"))
			print(presentation(available_task[task - 1](n), topics[task - 1]))
		
		def finder_2(func):
			i = str(input("\nEnter the range/ min & max value.\n(Put a comma(,) between the values)\n\nrange(min, max):"))
			input_pattern = r"(\d+)[\D\W]+(\d+)"
			analyzer = search(input_pattern, i)
			try:
				assert not analyzer
				min, max = int(analyzer.group(1)), int(analyzer.group(2))
			except:
				print("Invalid Input")
				MyMaths.perform()
			results = []
			for n in range(min, max + 1):
				if len(func(n)) > 0:
					results.append(n)
			print("\nBetween {0} and {1}, {2} can be expressed as {3}.\nThey are:".format(min, max, len(results), topics[task - 1]))
			for n in results:
				print(presentation(func(n), topics[task - 1]))
		
		def show_nth_fibonacci(func):
			n = input("Enter value of n: ")
			print(f'{n}th Fibonacci is {func(n)}')
		
		def searcher():
			i = str(input("\nEnter the range/ min & max value of search.\n(Put a comma(,) between the values)\nrange(min, max):"))
			input_pattern = r"(\d+)[\D\W]+(\d+)"
			analyzer = search(input_pattern, i)
			try:
				assert not analyzer
				min, max = int(analyzer.group(1)), int(analyzer.group(2))
			except:
				print("Invalid Input")
				MyMaths.perform()
			print("\nAvailable conditions to apply:\n1.Is an Even number.\n2.Is an Odd number\n3.Is a Prime Number.\n4.Is a Fibonacci Number.\n5.Is a Square number.\n6.Is a Cube Number.\n7.Infinitely Divisible by 2.\n8.Infinitely Divisible by 3.\n9.Infinitely Divisible by 4\n10.Infinitely Divisible by 5.\n11.Infinitely Divisible by 6.\n12.Infinitely Divisible by 9.\n13.Can be expressed as Sum of two squares.\n14.Can be expressed as Substraction of two squares.\n15.Can be expressed as Sum of two cubes.\n16.Can be expressed as Substraction of two cubes.\n17.Is the biggest in relevant range.\n18.Is the smallest in the relevant range.")
			s = str(input("\nEnter the number of conditions you want to apply.\nYou can select multiple conditions.\n(Put a comma(,) between the number of conditions)\nConditions: ")).split(",")
			conditions = []
			for k in s:
				try:
					n = int(k)
					conditions.append(n - 1)
				except:
					print("Invalid Input.Input should be like-\ncondition1, condition2,....")
					MyMaths.perform()
			try:
				assert all(i in conditions for i in [16, 17]) or all(i in conditions for i in [0, 1])
			except:
				MyMaths.perform()
			single_result = 0
			if single_result == 0 and any(x in conditions for x in [16, 17]):
				for i in conditions:
					if i in [16, 17]:
						single_result = i
						break
			if (len(conditions) > 7 or (len(conditions) > 4 and abs(max - min) >= 1500)) and single_result == 0:
				print("\nSearching.......\nPlease Wait\n")
			conditions.sort()
			available_conditions = [lambda n : n % 2 == 0, lambda n : n % 2 != 0, MyMaths.is_prime, MyMaths.is_fibonacci, MyMaths.is_square_number, MyMaths.is_cube_number, lambda n : n % 2 == 0, lambda n : n % 3 == 0, lambda n : n % 4 == 0, lambda n : n % 5 == 0, lambda n : n % 6 == 0, lambda n : n % 9 == 0, lambda n : len(MyMaths.as_sum_of_squares(n)) > 0, lambda n : len(MyMaths.as_substraction_of_squares(n)) > 0, lambda n : len(MyMaths.as_sum_of_cubes(n)) > 0, lambda n : len(MyMaths.as_substraction_of_cubes(n)) > 0]
			k = 1
			m, n = min, max + 1
			if 16 in conditions:
				m, n = max, min - 1
				k *= -1
			if any(i in conditions for i in [0, 1]):
				c = available_conditions[conditions[0]]
				m = m + 1 if not c(m) else m
				k *= 2
			results = []
			for i in range(m, n, k):
				if not any(con in conditions for con in [4, 5]) or 16 in conditions:
					num = i
				elif all(con in conditions for con in [4, 5]):
					num = i ** (2 * 3)
				elif 5 in conditions:
					num = i ** 3
				elif 4 in conditions:
					num = i ** 2
				elif 11 in conditions:
					num = i * 9
				elif 10 in conditions:
					num = i * 6
				elif 9 in conditions:
					num = i * 5
				elif 8 in conditions:
					num = i * 4
				elif 7 in conditions:
					num = i * 3
				elif 6 in conditions:
					num = i * 2
				if 16 in conditions:
					if num > max:
						continue
				elif num > max:
					break
				meets_conditions = True
				for i in conditions:
					if i in [16, 17]:
						continue
					if not available_conditions[i](num):
						meets_conditions = False
						break
				if meets_conditions:
					if single_result > 0:
						results = [num]
						break
					else:
						results.append(num)
			condition_types = ["Even", "Odd", "Prime", "Fibonacci", "Square", "Cube", "Infinitely Divisible by 2", "Infinitely Divisible by 3", "Infinitely Divisible by 4", "Infinitely Divisible by 5", "Infinitely Divisible by 6", "Infinitely Divisible by 9", "Sum of two squares", "Substraction of two squares", "Sum of two cubes", "Substraction of two cubes"]
			number_title = []
			sub_titles = []
			for y in conditions:
				if y < 6:
					if ("Prime" in number_title and y == 3) or ("Square" in number_title and y == 5):
						sub_titles.append(condition_types[y])
					else:
						number_title.append(condition_types[y])
			conditions = list(map(lambda x : condition_types[x], list(filter(lambda x : x >= 6 and x < 16, conditions))))
			if len(results) == 0:
				line = "Between {0} and {1}, no number was found meeting the conditions".format(min, max)
			elif single_result > 0:
				sub = "biggest" if single_result == 16 else "smallest"
				line = "\nBetween {0} and {1}, the {2}".format(min, max, sub)
				for title in number_title:
					line += " {0}".format(title)
				line += " number"
				if len(conditions) > 0 or len(sub_titles) > 0:
					line += " which"
				line = line + " is also a " + "Fibonacci number" if "Fibonacci" in sub_titles else line
				if len(sub_titles) > 1:
					line += " and"
				line = line + " is also a " + "Cube number" if "Cube" in sub_titles else line
				if len(conditions) > 0:
					added_1, added_2 = False, False
					for c in conditions:
						if "Infinitely" in c and not added_1:
							line += " is"
							added_1 = True
						elif not added_2:
							line += " can be expressed as"
							added_2 = True
						line += " " + c
						if conditions.index(c) == len(conditions) - 2:
							line += " and"
						elif conditions.index(c) < len(conditions) - 1:
							line += " ,"
				line += " is " + str(results[0])
			else:
				if len(results) == 1:
					aux, sub, quantity, res = "is", "number", "only one", ".It is " + str(results[0])
				else:
					aux, sub, quantity, res = "are", "numbers", str(len(results)), ".\nThey are :\n" + str(presentation(results))
				line = "\nBetween {0} and {1}, there {2} {3}".format(min, max, aux, quantity)
				for title in number_title:
					line += " " + title
				line = line + " which " + aux + " also Fibonacci" if "Fibonacci" in sub_titles else line
				line = line + " Cube " + sub if "Cube" in sub_titles and len(sub_titles) > 1 else line + " " + sub
				line = line + " which " + aux + " Cube " + sub if "Cube" in sub_titles and len(sub_titles) == 1 else line
				if len(conditions) > 0:
					if len(sub_titles) == 0:
						line += " which"
					else:
						line += " and"
					added_1, added_2 = False, False
					for c in conditions:
						if "Infinitely" in c and not added_1:
							line += " " + aux
							added_1 = True
						elif not added_2 and any(title in c for title in ["Sum", "Substraction"]):
							line += " can be expressed as"
							added_2 = True
						line += " " + c
						if conditions.index(c) == len(conditions) - 2:
							line += " and"
						elif conditions.index(c) < len(conditions) - 1:
							line += " ,"
				line += res
			print(line)
		
		available_task = [MyMaths.factors, MyMaths.prime_factors, MyMaths.is_prime, MyMaths.is_fibonacci, MyMaths.is_prime, MyMaths.is_fibonacci, MyMaths.prime_numbers, MyMaths.fibonacci_numbers, MyMaths.nth_fibonacci, MyMaths.gcd, MyMaths.lcm, MyMaths.is_square_number, MyMaths.is_cube_number, MyMaths.is_square_number, MyMaths.is_cube_number, MyMaths.square_numbers, MyMaths.cube_numbers, MyMaths.as_sum_of_squares, MyMaths.as_substraction_of_squares, MyMaths.as_sum_of_cubes, MyMaths.as_substraction_of_cubes, MyMaths.as_sum_of_squares, MyMaths.as_substraction_of_squares, MyMaths.as_sum_of_cubes, MyMaths.as_substraction_of_cubes]
		perform_task = [checker, checker, checker, checker, nearest, nearest, finder_1, finder_1, show_nth_fibonacci, calculator, calculator, checker, checker, nearest, nearest, finder_1, finder_1, expressor, expressor, expressor, expressor, finder_2, finder_2, finder_2, finder_2]
		if task == 1:
			n = int(input("\nEnter a number:"))
			print("\nFactors of {0} are : {1}".format(n,presentation(MyMaths.factors(n))))
		elif task == 2:
			n = int(input("\nEnter a number:"))
			print("\n", presentation(MyMaths.prime_factors(n), "prime factors"))
		elif task == 26:
			searcher()
		else:
			perform_task[task - 1](available_task[task - 1])
	
	@staticmethod
	def is_prime(n):
		if n in [2, 3, 5, 7]:
			return True
		elif n == 1 or n % 2 == 0 or n % 3 == 0:
			return False
		else:
			for k in range(5, n // 2, 2):
				if n % k == 0:
					return False
		return True
		
	@staticmethod
	def prime_numbers(*rng):
		if len(rng) == 1:
			strt = 1
			to = rng[0]
		elif len(rng) == 2:
			strt = rng[0]
			to = rng[1]
		else:
			strt, to = 1, 100
		for n in range(strt, to):
			if MyMaths.is_prime(n):
				yield n
	
	@staticmethod
	def is_fibonacci(n):
		a, b = 1, 1
		while b <= n:
			a, b = b, a + b
			if b == n:
				return True
		return  False
	
	@staticmethod
	def fibonacci_numbers(*rng):
		if len(rng) == 1:
			strt = 1
			to = rng[0]
		elif len(rng) == 2:
			strt = rng[0]
			to = rng[1]
		else:
			strt, to = 1, 2147483647
		if strt <= 1:
			a, b = 1, 1
			yield a
		else:
			a, b = strt - 1, strt
			while not MyMaths.is_fibonacci(a):
				a -= 1
			while not MyMaths.is_fibonacci(b):
				b += 1
		while b <= to:
			yield b
			a, b = b, a + b
	
	@staticmethod
	def nth_fibonacci(n):
		n = int(n)
		if n < 3:
			return 1
		return MyMaths.nth_fibonacci(n - 2) + MyMaths.nth_fibonacci(n - 1)
	
	@staticmethod
	def factors(n):
		for i in range(1, n + 1):
			if n % i == 0:
				yield i
	
	@staticmethod
	def prime_factors(n):
		if MyMaths.is_prime(n) or n == 1:
			yield 1
		while not MyMaths.is_prime(n) and n != 1:
			for i in range(2, n + 1):
				if n % i == 0:
					n = n // i
					yield i
					break
		yield n
	
	@staticmethod
	def gcd(*nums):
		res = min(nums)
		while res > 0:
			if all(n % res == 0 for n in nums):
				return res
			res -= 1
	
	@staticmethod
	def lcm(*nums):
		F = [list(MyMaths.prime_factors(n)) for n in nums]
		factors = []
		for currect_list in F:
			biggest = True
			for comparing_list in F:
				if currect_list == comparing_list:
					continue
				if len(comparing_list) > len(currect_list):
					biggest = False
					break
			if biggest:
				F.remove(currect_list)
				factors = currect_list
				break
		for n in factors:
			for comparing_list in F:
				if n in comparing_list:
					comparing_list.remove(n)
		for current_list in F:
			factors += current_list
		res = 1
		for n in factors:
			res *= n
		return res
	
	@staticmethod
	def is_square_number(n):
		return int(n ** 0.5) ** 2 == n
	 
	@staticmethod
	def is_cube_number(n):
		return int(n ** 0.3333334) ** 3 == n
	
	@staticmethod
	def square_numbers(*rng):
		if len(rng) == 1:
			strt = 1
			to = rng[0]
		elif len(rng) == 2:
			strt = rng[0]
			to = rng[1]
		else:
			strt, to = 1, 100
		for i in range(strt, to):
			n = i ** 2
			if n >= strt and n <= to:
				yield n
			else:
				break
	
	@staticmethod
	def cube_numbers(*rng):
		if len(rng) == 1:
			strt = 1
			to = rng[0]
		elif len(rng) == 2:
			strt = rng[0]
			to = rng[1]
		else:
			strt, to = 1, 100
		for i in range(strt, to):
			n = i ** 3
			if n >= strt and n <= to:
				yield n
			else:
				break
	
	@staticmethod
	def is_whole_power_number(power, n):
		return int(n ** (1 / power)) ** power == n
	
	@staticmethod
	def as_sum_of_squares(num):
		results = []
		possibility = False
		for n in range(1, num):
			m = num - (n ** 2)
			if m <= 0:
				break
			if MyMaths.is_whole_power_number(2, m):
				possibility = True
				m = int(m ** (0.5))
				res = tuple(sorted([m, n], reverse=True))
				if (m ** 2) + (n ** 2) == num:
					results.append(res)
		if possibility:
			return list(set(results))
		else:
			return list([])
	
	@staticmethod
	def as_sum_of_cubes(num):
		results = []
		possibility = False
		for n in range(1, num):
			m = num - (n ** 3)
			if m <= 0:
				break
			if MyMaths.is_whole_power_number(3, m):
				possibility = True
				m = int(m ** (1 / 3))
				res = tuple(sorted([m, n], reverse=True))
				if (m ** 3) + (n ** 3) == num:
					results.append(res)
		if possibility:
			return list(set(results))
		else:
			return list([])
	
	@staticmethod
	def as_substraction_of_squares(num):
		results = []
		for i in MyMaths.factors(num):
			if i >= len(list(MyMaths.factors(num))):
				break
			a, b = i, num // i
			if a != b:
				a, b = (a + b) // 2, abs((a - b) // 2)
				if (a ** 2) - (b ** 2) == num:
					results.append(tuple(sorted([a, b], reverse=True)))
		return list(set(results))
	
	@staticmethod
	def as_substraction_of_cubes(num):
		factors = list(MyMaths.factors(num))
		results = []
		for x in reversed(factors[0: math.ceil(len(factors) / 2)]):
			y = num / x
			b = x / 2
			a = math.sqrt(abs(y - (b ** 2)) / 3)
			p, q = abs(int(a + b)), abs(int(a - b))
			k = (p ** 3) - (q ** 3)
			if k == num and not 0 in [p, q]:
				results.append((int(p), int(q)))
		return list(set(results))

class presentation:
	#should be define with parameters : (item to present, title[optional], subject/type[not required for lists])
	#available type/subjects: "prime factors", "list", "sum of squares", "substraction of squares", "sum of cubes"
	def __init__(self, item, m = "list", k = None):
		self.subject = m.lower()
		self.title = k
		self.to_present = item
	
	def prime_factors(self):
		as_string = ""
		factors = list(self.to_present)
		i = 0
		k = 1
		for n in factors:
			k *= n
			as_string += str(n)
			if i < len(factors) - 1:
				as_string += " * "
			i += 1
		self.title = k
		return str(self.title) + " = " + as_string
	
	def lists(self):
		as_string = ""
		items = list(self.to_present)
		for item in items:
			as_string += str(item)
			if items.index(item) == len(items) - 2:
				as_string += " and "
			elif items.index(item) != len(items) - 1:
				as_string += ", "
		return as_string
	
	def as_sum_of_squares(self):
		if len(self.to_present) > 0:
			self.title = (self.to_present[0][0] ** 2) + (self.to_present[0][1] ** 2)
			as_string = str(self.title)
			for pair in self.to_present:
				as_string += " = {0}^2 + {1}^2".format(pair[0], pair[1])
		else:
			as_string = "This number cannot be expressed as sum of two squares"
		return as_string
		
	def as_substraction_of_squares(self):
		if len(self.to_present) > 0:
			self.title = (self.to_present[0][0] ** 2) - (self.to_present[0][1] ** 2)
			as_string = str(self.title)
			for pair in self.to_present:
				as_string += " = {0}^2 - {1}^2".format(pair[0], pair[1])
		else:
			as_string = "This number cannot be expressed as substraction of two squares"
		return as_string
	
	def as_sum_of_cubes(self):
		if len(self.to_present) > 0:
			self.title = (self.to_present[0][0] ** 3) + (self.to_present[0][1] ** 3)
			as_string = str(self.title)
			for pair in self.to_present:
				as_string += " = {0}^3 + {1}^3".format(pair[0], pair[1])
		else:
			as_string = "This number cannot be expressed as sum of two cubes"
		return as_string
	
	def as_substraction_of_cubes(self):
		if len(self.to_present) > 0:
			self.title = abs((self.to_present[0][0] ** 3) - (self.to_present[0][1] ** 3))
			as_string = str(self.title)
			for pair in self.to_present:
				as_string += " = {0}^3 - {1}^3".format(pair[0], pair[1])
		else:
			as_string = "This number cannot be expressed as sum of two cubes"
		return as_string
		
	
	funcs = {"prime factors": prime_factors,"list": lists, "sum of two squares": as_sum_of_squares, "substraction of two squares": as_substraction_of_squares, "sum of two cubes":  as_sum_of_cubes, "substraction of two cubes": as_substraction_of_cubes}
	
	def __repr__(self):
		return self.funcs[self.subject](self)

if __name__ == "__main__":
	MyMaths.perform();