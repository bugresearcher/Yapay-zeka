#!/usr/bin/env python3
import parser
import urllib.parse
import requests
import requests.exceptions
import sozluk
import random
from termcolor import colored, cprint

def main():
	while 1:
		ara = input("Aranan : ")
		if ara == ":q":
			break
		sonuc = dict2(ara)
		if isinstance(sonuc,list):
			for i in sonuc:
				cprint(i,color_sec())
	return 0

def dict2(aranan):
	return sozluk.control(aranan)

def color_sec():
	renk = ["grey","red","green","yellow","blue","magenta","cyan","white"]
	return random.choice(renk)
	

if __name__ == "__main__":
    main()
