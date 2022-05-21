import requests
import csv
import threading

#dir_file = ['admin','Image','Index','Internet','Java','Legal','Links','Login','MANIFEST']

link = input("ENTER THE TARGET LINK WITH (HTTP OR HTTPS://):")

file_path = input("ENTER THE WORDLIST FILE PATH:")

#word_list = []

def attack(name):

	with open(file_path, 'r') as f:
		word_list = f.read()

	for word in word_list:
		req = requests.get(link+'/'+word) 

		status_code = req.status_code

		print(f"{link}/{word} : {status_code}")

threads = 62

while threads >= 1:
    t = threading.Thread(target=attack,args=(threads,))
    t.start()
    threads -=1

#attack(link,file_path)

	


#C:\Users\JASWANTH\OneDrive\Desktop\wordlist.txt
#https://www.saranathan.ac.in



