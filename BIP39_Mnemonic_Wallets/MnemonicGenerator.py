import hashlib
import binascii

# Word list comes from here:
# https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
text_file = open("wordList.txt", "r")
wordList = text_file.read().split(',')
text_file.close()


userInput = input("Enter your 256 bits then hit \"Enter\":\n ")
inputLength=len(userInput)
if inputLength != 256:
  print("\nInput was not exactly 256 bits, it was instead",inputLength)
  quit()

print("\nNumber of bits you provided: \n",inputLength)
bits="0b"+userInput
a=int(bits, 2)

entropy_bytes = int.to_bytes(a, length=32, byteorder="big")
sha256_bytes = bytes(hashlib.sha256(entropy_bytes).digest())
hexResult = binascii.hexlify(sha256_bytes)
print("\n256 bits hashed with sha256, now represented in hexadecimal:\n",hexResult,"\n")
firstTwo = hexResult.decode("utf-8")[:2]
print("2 most significant digits aka \"2 most significant nibbles\": ",firstTwo,"\n")
checksum =bin(int(firstTwo, 16))[2:].zfill(8)
print("----------------------")
print("CHECKSUM --->",checksum)
print("----------------------\n")

bits=userInput
bits += checksum

ElevenBits = ""
WordNumbers=[]
WordCounter=0
mnemonics = []
for num in range(1,265):
  ElevenBits += bits[num-1]
  decimal = int(ElevenBits, 2)
  if num % 11 == 0:
    WordNumbers.append(decimal)
    WordCounter=WordCounter+1
    mnemonics.append(wordList[decimal])
    print("word #",WordCounter," ---> ",ElevenBits," -----> ",decimal," ---> ",wordList[decimal],"\n");
    ElevenBits = ""

print("     YOUR 24 WORDS")
print("----------------------")
for word in mnemonics:
  print("       ",word)
print("----------------------")