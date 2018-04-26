import pyperclip
 
plaintext = 'PNRFNEPVCURE.'
 
key = 10
 
mode = 'decrypt' 
 
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
translated = ''

plaintext = plaintext.upper()
 
for symbol in plaintext:
	if symbol in letters:
		num = letters.find(symbol) 
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key

		if num >= len(letters):
			num = num - len(letters)
		elif num < 0:
			num = num + len(letters)
		translated = translated + letters[num]

else:
		translated = translated + symbol
 
print(translated)
 
pyperclip.copy(translated)

#python3 decrypt.py
