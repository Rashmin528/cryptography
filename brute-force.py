plaintext = 'MKOCKBMSZROB.'

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(letters)):

	translated = ''

	for symbol in plaintext:
		if symbol in letters:
			num = letters.find(symbol) 
			num = num - key

			if num < 0:
				num = num + len(letters)
			translated = translated + letters[num]
		else:
			translated = translated + symbol
	print('%s %s' % (key, translated))

#python3 brute-force.py

