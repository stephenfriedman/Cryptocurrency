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
# convert the input string to the binary representation
binary=int(bits, 2)

# Convert to bytes
entropy_bytes = int.to_bytes(binary, length=32, byteorder="big")
# Use sha256 on the bytes
sha256_bytes = bytes(hashlib.sha256(entropy_bytes).digest())
# Return the hexadecimal representation of the binary data
hexResult = binascii.hexlify(sha256_bytes)
print("\n256 bits hashed with sha256, now represented in hexadecimal:\n",hexResult,"\n")
# Take the two significant nibbles
firstTwo = hexResult.decode("utf-8")[:2]
print("2 most significant digits aka \"2 most significant nibbles\": ",firstTwo,"\n")
# The checksum is the conversion of these 2 nibbles into binary
checksum =bin(int(firstTwo, 16))[2:].zfill(8)
print("----------------------")
print("CHECKSUM --->",checksum)
print("----------------------\n")

bits=userInput
#  Append our 8 bit checksum onto our 256 bits of entropy for a total of 264 bits
bits += checksum

ElevenBits = ""
WordNumbers=[]
WordCounter=0
mnemonics = []
# Each 11 bits, convert the binary to ascii and find corresponding word from the list
for num in range(1,265):
  ElevenBits += bits[num-1]
  decimal = int(ElevenBits, 2)
  # Split up the 256 bits into 24 11 bit pieces
  if num % 11 == 0:
    WordNumbers.append(decimal)
    WordCounter=WordCounter+1
    mnemonics.append(wordList[decimal])
    print("word #",WordCounter," ---> ",ElevenBits," -----> ",decimal," ---> ",wordList[decimal],"\n");
    ElevenBits = ""

# Print out the 24 words
print("     YOUR 24 WORDS")
print("----------------------")
for word in mnemonics:
  print("       ",word)
print("----------------------")