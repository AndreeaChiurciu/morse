import argparse, sys, unittest

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

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help='outputfile', nargs= 1, required=True)
    parser.add_argument('-i', help='inputfile', nargs='+', required=True)
    parser.add_argument('-a', action='store_true', default=False,
                    dest='ASCII2MORSE',help='ASCII -> Morse')
    parser.add_argument('-m', action='store_true', default=False,
                    dest='MORSE2ASCII', help='Morse -> ASCII')
    parser.add_argument('--version', action='version', version='0.1')
    args = parser.parse_args()

    if args.ASCII2MORSE :
       msg = raw_input('ASCII to Morse conversion: ')
       if not verify(msg):
          sys.exit('Error message cannot be translated to Morse Code')
       print encodeToMorse(msg)
    else :
       msg = raw_input('Morse to ASCII conversion: ')
       print decodeMorse(msg)

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
    main()
    #unittest.main()
