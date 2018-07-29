import math, pyperclip

def main():
	myMessage = 'Hreatrphnpdayan ydb oiF.'
	myKey = 8
	plaintext = decryptMessage(myKey, myMessage)
	
	print(plaintext + '|')
	
	pyperclip.copy(plaintext)

def decryptMessage(Key, message):
	numOfColumns = math.ceil(len(message) / Key)
	numOfRows = Key
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	plaintext = [''] * numOfColumns
	col = 0
	row = 0
	
	for symbol in message:
		plaintext[col] += symbol
		col += 1
		
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1
	return ''.join(plaintext)

if '__main__' == '__main__':
	main()
