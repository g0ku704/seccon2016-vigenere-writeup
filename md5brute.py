#!/usr/bin/python
import hashlib
import itertools
import sys

resultmd5 = "f528a6ab914c1ecf856a1d93103948fe"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
charsetlist = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z { }".split(" ")

charsetlist_1 = "ABC"
charsetlist_2 = "FGHIJKL"
charsetlist_3 = "QRSTUVW"

plaintext_1 = "SECCON{A"
plaintext_2 = "BCDEDEFG"
plaintext_3 = "KLMNOPQR"
plaintext_4 = "VWXYYZ}"

def brute_force(value):
	if hashlib.md5(value.encode("UTF-8")).hexdigest() == resultmd5:
		return true
plain = ""
for c1 in itertools.product(charsetlist_1,repeat=4):
	for c2 in itertools.product(charsetlist_2,repeat=4):
		for c3 in itertools.product(charsetlist_3,repeat=4):
			plain = plaintext_1 + ''.join(c1) + plaintext_2 + ''.join(c2) + plaintext_3 + ''.join(c3) + plaintext_4
			print("Now trying: " + plain)
			if(brute_force(plain)):
				print("FOUND: " + plain)
				sys.exit(0)

