#!/usr/bin/python3

def caesar(plaintext, shift):
	ciphertext = ''
	for i in plaintext:
		if 97 <= ord(i) <= 122:
			ciphertext += chr((ord(i) - 97 + shift)%26 + 97)
		else:
			ciphertext += i
	return ciphertext

def xored_list(str1, str2):
	return [ord(a) ^ ord(b) for a,b in zip(str1, str2)]

plaintext = input("String to be encrypted: ")
key = <Redacted to make it impossible to break>

sixth_shift = caesar(plaintext, 6)
xored = xored_list(sixth_shift, key*3)

if xored == [11, 56, 13, 88, 12, 65, 54, 21, 107, 86, 14, 17, 61, 40, 78, 24, 74, 60, 56, 63, 27, 98, 59, 34, 70, 64, 68, 68]:
	print('Impossible!')
else:
	print('Mwahahaha... You\'ll need to go back in time to get this')