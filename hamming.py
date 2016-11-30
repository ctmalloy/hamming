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
    #
    # Title: Encode
    # Parameter: 's' represents a bitString
    # Output: Check bits for each parity bit and the encoded bitStream
    #
    def encode(self, s):
        parity = 0
        self.bitString = s
        length = len(s)                             # Length of bitString
        streamLength = length + parity              # Length of transmission
        # Calculate number of Parity Bits
        while True:
            if (streamLength+1) <= 2**parity:
                break
            parity += 1
        streamLength = length + parity              # Update Length of transmission
        p = 0            
        p0 = 0
        j = 0                                       # Iterator for bitString
        bitStream = [0] * (streamLength+1)          # Initialize data type
        # Re-Map bitString in bitStream
        for i in range(1, streamLength+1):
            p0 = 2**p
            if i % p0 != 0:
                bitStream[i] = int(s[j])
                j+=1
            else:
                p+=1
        # Calculate parity bit from respective check bits
        for i in range(parity):
            sIncrement = 2**i
            bIncrement = sIncrement * 2
            n = sIncrement
            checkBits = []
            print("\nParity Bit", sIncrement)
            # Calculate check bits
            while True:
                for i in range(n,(sIncrement+n)):
                    checkBits.append(i)
                    if i > streamLength:
                        break
                    bitStream[sIncrement] ^= bitStream[i]
                if i > streamLength:
                    break
                else:
                    n += bIncrement
            print("Check Bits: ", checkBits)  # Displays check bits for parity
        # Display Hamming Encoded bit stream
        print("\nHamming Encoded Message: ", bitStream[1:])
#
#####........ Main ........#####
if __name__=="__main__":
    # Prompt for input of bitString
    bitString = input("Enter a bit string between 1 and 64bits in length: ")
    # Hamming Function
    hamming = Hamming(bitString)
#
#
#