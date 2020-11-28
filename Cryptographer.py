import sys

def shift_char(char, shift, reverse=False):
	if char.isspace():
		return char
	char_ascii = ord(char)
	if type(shift) is str:
		shift = ord(shift.upper()) - 65
	shift = shift * -1 if reverse else shift
	if abs(shift) >= 26:
		shift %= 26
	new_ascii = char_ascii + shift
	if char.islower():
		if new_ascii > 122:
			new_ascii = 97 + (new_ascii - 123)
		elif new_ascii < 97:
			new_ascii = 122 - (96 - new_ascii)
	elif char.isupper():
		if new_ascii > 90:
			new_ascii = 65 + (new_ascii - 91)
		elif new_ascii < 65:
			new_ascii = 90 - (64 - new_ascii)
	return chr(new_ascii)

def decimal(num, base=2):
	dec = 0
	negative = False
	for pow, n in enumerate(num[::-1]):
		if n.isalpha():
			n = 10 + (ord(n.upper()) - 65)
		else:
			n = int(n)
		k = n * (base ** pow)
		dec += k
	if negative:
		dec *= -1
	return dec

def non_decimal(dec, base=2):
	non_dec = ""
	negative = False
	dec = int(dec)
	while dec != 0:
		k = dec % base
		dec = dec // base
		if k > 9:
			l = chr(65 + (k - 10))
			non_dec += l
		else:
			non_dec += str(k)
	non_dec = non_dec[::-1]
	if negative:
		non_dec = "-" + non_dec
	return non_dec

def encrypted_Caeser(text, shift=3):
	encrypted_text = ""
	for letter in text:
		letter = shift_char(letter, shift)
		encrypted_text += letter
	return encrypted_text
	
def decrypted_Caeser(text, shift=3):
	decrypted_text = ""
	for letter in text:
		letter = shift_char(letter, shift * -1)
		decrypted_text += letter
	return decrypted_text

def converted(text, base=2):
	convt = []
	for letter in text:
		ascii = ord(letter)
		encrp = non_decimal(ascii, base)
		if len(encrp) < 7 and base == 2:
			encrp = ((7 - len(encrp)) * '0') + encrp
		convt.append(encrp)
	return ' '.join(convt)

def to_text(text, base=2):
	plain_text = ""
	for chunk in text.split():
		ascii = decimal(chunk, base)
		letter = chr(ascii)
		plain_text += letter
	return plain_text

def encrypted_Vigenere(text, key):
	encrypted_text = ""
	i = 0
	for letter in text:
		i = 0 if i >= len(key) else i
		shift = key[i]
		letter = shift_char(letter, shift)
		i += 1
		encrypted_text += letter
	return encrypted_text

def decrypted_Vigenere(text, key):
	decrypted_text = ""
	i = 0
	for letter in text:
		i = 0 if i >= len(key) else i
		shift = key[i]
		letter = shift_char(letter, shift, True)
		i += 1
		decrypted_text += letter
	return decrypted_text

def xor(x, y):
	xored = ""
	for a, b in zip(x, y):
		if a.isspace():
			xored += ' '
			continue
		new = int(a) ^ int(b)
		xored += str(new)
	return xored

def encrypted_OTP(text, key):
	if len(text) != len(key):
		key *= (len(text) // len(key)) + 1
	binary_text = converted(text)
	binary_key = converted(key)
	encrypted_text = xor(binary_text, binary_key)
	if to_text(encrypted_text).count(' ') == text.count(' '):
		if all(ord(char) in range(32, 127) for char in to_text(encrypted_text)):
			encrypted_text = to_text(encrypted_text)
	return encrypted_text

def decrypted_OTP(encrypted_text, key):
	if len(encrypted_text) != len(key):
		key *= (len(encrypted_text) // len(key)) + 1
	if not all(l in ['0', '1', ' '] for l in key):
		key = converted(key)
	if any(l not in ['0', '1', ' '] for l in encrypted_text):
		encrypted_text = converted(encrypted_text)
	decrypted_binary = xor(encrypted_text, key)
	decrypted_text = to_text(decrypted_binary)
	return decrypted_text


def execute():
	try:
		if len(sys.argv) > 1:
			if len(sys.argv) in [4, 5]:
				commands = sys.argv[1:]
			else:
				commands = sys.argv[1]
				commands = commands.split(",")
		else:
			print("""Available Cryption Types:
1.ASCII
2.Binary
3.Octal
4.Hexadecimal (or Hex)
5.Caeser Cipher
6.Vigenere Cipher
7.One Time Pad (or OTP)""")

			print("\nCommand Format(Commas are required, No Curly Braces):\n{\'de\'(to decrypt) or \'en\'(to encrypt)}, {Cryption type name or number from above}, {key(if required)}, {text}")
			commands = input("\nEnter command in the format above:\n")
			commands = commands.split(",")
		commands = list(map(str.strip, commands))
		
		action = commands[0][:2].lower()
		if action not in ['de', 'en']:
			raise Exception("Unknown Command " + commands[0])
		
		types = ['ascii', 'binary', 'octal', 'hexadecimal', 'caeser', 'vigenere', 'one time pad']
		encrypters = [converted, converted, converted, converted, encrypted_Caeser, encrypted_Vigenere, encrypted_OTP]
		decrypters = [to_text, to_text, to_text, to_text, decrypted_Caeser, decrypted_Vigenere, decrypted_OTP]
		
		cryption_type = None
		if str(commands[1]).isnumeric():
			cryption_type = int(commands[1]) - 1
		else:
			if commands[1].lower() == 'otp':
				cryption_type = 6
			elif commands[1] in types:
				cryption_type = types.index(commands[1])
			else:
				for t in types:
					if t.lower().startswith(commands[1]):
						cryption_type = types.index(t)
		if type(cryption_type) is None or cryption_type not in range(8):
			raise Exception("Unknown Cryption Type")
		if cryption_type < 0:
			cryption_type *= -1
		
		if cryption_type < 4 and len(commands) < 3:
			raise Exception("Invalid Input")
		elif cryption_type > 4 and len(commands) < 4:
			raise Exception("Invalid Input")
		
		if cryption_type == 0:
			key = 10
		if cryption_type == 1:
			key = 2
		elif cryption_type in [2, 3]:
			key = 2 ** (cryption_type + 1)
		elif cryption_type == 4:
			if len(commands) == 4:
				try:
					key = int(commands[-2])
				except ValueError:
					raise Exception("Invalid Key, Key must be an integer")
			else:
				key = 3
		elif cryption_type > 4:
			key = commands[-2]
		
		text = commands[-1]
		output_text = ""
		
		if action == 'en':
			output = encrypters[cryption_type](text, key)
			status = "Converted Form" if cryption_type < 4 else "Encrypted Form"
		elif action == 'de':
			output = decrypters[cryption_type](text, key)
			status = "Decrypted Form"
		
		print(f"\n{status}:\n{output}")
		
	except Exception as exp:
		print("Error:", exp, "\nRestarting Programme.....\n")
		execute()
		

if __name__ == "__main__":
	execute()