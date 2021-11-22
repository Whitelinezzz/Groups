from fileinput import filename
import csv
import sys
open("Группа3.txt","w").write(open("Группа1.txt","r").read() + open("Группа2.txt","r").read())
filename = ("C:\\Users\\YO\\Downloads\\Группа1.txt")
text_file = open ("C:\\Users\\YO\Downloads\\Группа1.txt",'r')
reader=csv.reader(text_file,delimiter="t")
for str in reader:
 print (str)
text_file.close()

from fileinput import filename
import csv
import sys
filename = ("C:\\Users\\YO\\Downloads\\Группа2.txt")
text_file = open ("C:\\Users\\YO\Downloads\\Группа2.txt",'r')
reader=csv.reader(text_file,delimiter="t")
for str in reader:
 print (str)
text_file.close()

from fileinput import filename
import csv
import sys
filename = ("C:\\Users\\YO\\Downloads\\Группа3.txt")
text_file = open ("C:\\Users\\YO\Downloads\\Группа3.txt",'r')
reader=csv.reader(text_file,delimiter="t")
def sortByAlphabet(inputStr):
        return inputStr[0]
for str in reader:
 print (str)
text_file.close()