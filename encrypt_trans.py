import pyperclip

def main():
	plaintext = 'Happy birthday Fernando.'
	Key = 8
	ciphertext = encryptMessage(Key, plaintext)
	
	print(ciphertext + '|')
	
	pyperclip.copy(ciphertext)

def encryptMessage(key, message):
	ciphertext = [''] * key
	for col in range(key):
		pointer = col
		while pointer <len(message):
		
			ciphertext[col] += message[pointer]
			pointer +=key
	return ''.join(ciphertext)

if '__main__' == '__main__':
	main()
