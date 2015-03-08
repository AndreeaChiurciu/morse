import sys
import unittest

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' ,
        
        ' ':'$'
        }


inverseMorseAlphabet=dict((v,k) for (k,v) in CODE.items())

def verify(string):
    keys = CODE.keys()
    for char in string:
        if char.upper() not in keys:
           return False
    return True


# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString = 0):
	if positionInString < len(code):
		morseLetter = ""
		for key,char in enumerate(code[positionInString:]):
			if char == " ":
				positionInString = key + positionInString + 1
				letter = inverseMorseAlphabet[morseLetter]
				return letter + decodeMorse(code, positionInString)
			else:
				morseLetter += char
	else:
		return ""

#encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
	encodedMessage = ""
	for char in message[:]:
		encodedMessage += CODE[char.upper()] + " "
	return encodedMessage 

def main(argv):
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv, 'o:i:')
    except getopt.GetoptError:
		sys.stderr.write('Usage ' + sys.argv[0] + '[-a | -m] [ -i inputfile ] [ -o outfile ] \n')
		sys.exit(1)

    msg = raw_input('MESSAGE: ')
    
    if not verify(msg):
		sys.exit('Error message cannot be translated to Morse Code')

    print encodeToMorse(msg)

class MyTest(unittest.TestCase):
    # Ref issue #9
    def test_toMorse(self):
        self.assertMultiLineEqual(encodeToMorse('SOS'), '... --- ... ')
    
    # Ref issue #9
    def test_toASCII(self):
		self.assertMultiLineEqual(decodeMorse('... --- ... $ .-.. . $ -- --- -. -.. . '), 'SOS LE MONDE')
    
    def test_verify(self):
        self.assertFalse(verify(';'))
        self.assertTrue(verify('SOS LE MONDE'))

        
if __name__ == "__main__":
    main(sys.argv[1:])
    #unittest.main()
