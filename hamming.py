# 
# File: hamming.py
# Author: Conner Malloy
# Date: November 28, 2016
# 
# Program: Hamming
# 
# Determines the number of parity bits based on the length of the bit
# string 's' and calculates checkbits to encode and display Hamming Code
#
class Hamming:
    def __init__(self, bits):
        self.bits = bits
        self.bitStream = []
        self.encode(bits)

    def encode(self, s):
        r = 0
        self.bitString = s
        length = len(s)
        # Calculate number of Parity Bits
        while True:
            if (length+r+1) <= 2**r:
                break
            r += 1
        streamLength = length + r                   # Length of transmission
        temp = 0            
        temp2 = 0
        j = 0                                       # Iterator for bitString
        bitStream = [0] * (streamLength+1)          # Initialize data type
        # Re-Map bitString in bitStream
        for i in range(1, streamLength+1):
            temp2 = 2**temp
            if i % temp2 != 0:
                bitStream[i] = int(s[j])
                j+=1
            else:
                temp+=1
        # Calculate parity bit from respective check bits
        for i in range((r)):
            sIncrement = 2**i
            bIncrement = sIncrement * 2
            start = sIncrement
            checkPos = start
            checkBits = []
            print("\nParity Bit", sIncrement)
        # Calculate check bits
            while True:
                for i in range(start,(start+sIncrement)):
                    checkPos = i
                    checkBits.append(checkPos)
                    if i > streamLength:
                        break
                    bitStream[sIncrement] ^= bitStream[checkPos]
                if checkPos > streamLength:
                    break
                else:
                    start = start + bIncrement
            print("Check Bits: ", checkBits)  # Displays check bits for parity
        # Display Hamming Encoded bit stream
        print("\nHamming Encoded Message: ", bitStream[1:])

    #####........ Main ........#####
if __name__=="__main__":
    # Prompt for input of bitString
    bitString = input("Enter a bit string between 1 and 64bits in length: ")
    # Hamming Function
    hamming = Hamming(bitString)

