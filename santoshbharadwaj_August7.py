'''
Write a program to determine largest command line input
1) py prog2.py 10 20 30.8 7 40 35.6
 What is the largest command line input ? ---> 40
 What is argv ? ---> ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
 What is list 'a' ? ---> [10 , 20 , 30.8 , 7 , 40 , 35.6]
 How to determine largest element of list 'a' ? ---> max(a) i.e. 40
 What is the result of max(argv[1:]) ? ---> '7'
 What is the issue with max(argv[1:])) ? --->
Largest string is obtained but not largest number
2) py prog2.py
 What is the output ? ---> Pls send inputs
3) py prog2.py 'Rama' 'Sita' 'Rajesh' 'Manohar' 'Vamsi' 'Amar'
 What is the largest command line input ? ---> 'Vamsi'
4) py prog2.py 25 'Ten'
 What is the output ? ---> Inputs can not be number and string
5) Hint1: Use for loop
6) Hint2: Use try and except
'''
import sys
try:
 args = sys.argv[1:]
 if not args:
 print("Please send inputs")
 sys.exit()
 try:
 a = [float(x) for x in args]
 print("argv :", args)
 print("List a:", a)
 print("Largest command line input:", max(a))
 except ValueError:
 if all(x.isalpha() for x in args):
 print("argv :", args)
 print("Largest command line input:", max(args))
 else:
 print("Inputs cannot be both numbers and strings together")
except Exception as e:
 print("Error:", e)
'''
Write a program to determine command line input is even number or odd number
1) py prog3.py 26
 What is the output ? ---> Even number
2) py prog3.py 45
 What is the output ? ---> Odd number
3) py prog3.py
 What is the output ? ---> Pls send an integer input
4) py prog3.py 10.8
 What is the output ? ---> Pls send an integer input
5) py prog3.py Ten
 What is the output ? ---> Pls send an integer input
'''
import sys
try:
 if len(sys.argv) != 2:
 print("Pls send an integer input")
 else:
 num = int(sys.argv[1])
 if num % 2 == 0:
 print("Even number")
 else:
 print("Odd number")
except ValueError:
 print("Pls send an integer input")
'''
Write a program to determine average of command line inputs
1) py prog4.py 10.8 25 True 14.6 19 False 7.4
 What is argv ? --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
 What is list 'a' ? ---> [10.8 , 25 , True , 14.6 , 19 , False , 7.4]
How to determine sum of list elements ? ---> sum(a)
 How to determine number of list elements ? ---> len(a)
2) py prog4.py
 What is the output ? ---> Pls send number inputs
3) py prog4.py 25 'Ten'
 What is the output ? ---> Pls send number inputs
'''
import sys
try:
 args = sys.argv[1:]
 if not args:
 print("Pls send number inputs")
 sys.exit()
 try:
 a = [float(x) for x in args]
 avg = sum(a) / len(a)
 print("argv:", sys.argv)
 print("List a:", a)
 print(f"Average: {avg}")
 except ValueError:
 print("Pls send number inputs")
except Exception as e:
 print("Error:", e)
'''
Write a program to sort command line inputs in ascending order and descending order
1) py prog5.py 10 20 15.8 5 12.6
 What is argv ? ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
 What is list 'a' ? ---> [10 , 20 , 15.8 , 5 , 12.6]
 How to sort list 'a' ? ---> sorted(a)
 How to sort list 'a' in descending order ? ---> sorted(a , reverse = True)
2) py prog5.py 25 'Ten'
 What is the output ? ---> Pls don't send number and string inputs together
'''
import sys
args = sys.argv[1:]
try:
 if not args:
 print("Pls send number inputs")
 sys.exit()
 try:
 a = [float(x) for x in args]
 print("argv:", sys.argv)
 print("List a:", a)
 print("Ascending order:", sorted(a))
 print("Descending order:", sorted(a, reverse=True))
 except ValueError:
 if all(x.isalpha() for x in args):
 print("argv:", sys.argv)
 print("List a:", args)
 print("Ascending order:", sorted(args))
 print("Descending order:", sorted(args, reverse=True))
 else:
 print("Pls don't send number and string inputs together")
except Exception as e:
 print("Error:", e)
# Find outputs (Home work)
print( 'green' in 'Hyd is green city')#True => ‘green’ is exactly as written
print('day' in 'Sankar dayal sarma')#True
print('Green' in 'Hyd is green city')#False
print('d is' in 'Hyd is green city')#True
print('dis' in 'Hyd is green city')#False
print('iniv' in 'Srinivas')#True
print('iniv' not in 'Srinivas')#False 
''' (Home work)
Slice demo program
0 1 2 3 4 5 6 7
R a m a R a o
-8 -7 -6 -5 -4 -3 -2 -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#Rm a
print(a [ : 7])#Rama Ra
print(a [2 : 4])#ma
print(a [2 : ])#ma Rao
print(a [ : 4 ])#Rama
print(a [ : : 2])#Rm a
print(a [-6 : -1])#ma Ra
print(a [-6 : ])#ma Rao
print(a [: -4 : -1])#oa
print(a [-3 : -1]) # a[-3 : -1 : 1] ---> string from indexes -3 to -2 in steps of 1 i.e. Ra
print(a [-3 : ])#Rao
print(a [ : : ])#Rama Rao
print(a [ : ])#Rama Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2])#oRaa
print(a [ -2 : : -2]) # a[-2 : -9 : -2] ---> string from indexes -2 to -8 in steps of -2 i.e. a<space>mR
print(a [2 : 8])#ma Rao
print(a [2 : 8 : -1])#empty
print(a [ : -6 : -1])#oaR
print(a [2 : -3])#ma
print(a [1 : 6 : 2])#aaR
print(a [ : -5 : -5])#o
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oaR ama
print(a [-5 : 0 : -2])#aa
'''
Write a program to concatenate two strings separated by space but swap first two
characters of the two strings.
Assume that each string has a minimum of two characters
Let inputs be Java and Python
What are the outputs ? ---> Pyva<space>Jathon
Hint: Use slice
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
result = new_s1 + " " + new_s2
print(result)
'''
Write a program to print first two and the last two characters of the string
Print an empty string if string has less than four characters
1) Let input be PYTHON
 What is the output ? ---> PYON
2) Let input be Hyd
 What is the output ? ---> Nothing
'''
s1 = input("Enter the string: ")
if len(s1) < 4: 
 print("Nothing") 
else:
 new_s1 = s1[:2] + s1[-2:] 
 print(new_s1)
'''
Write a program to print characters of the string in forward and reverse
directions without slice
 0 1 2 3 4
Let input be V A M S I
 -5 -4 -3 -2 -1
What are the outputs ? ---> 
Character at index 0 : V
Character at index 1 : A 
Character at index 2 : M 
Character at index 3 : S 
Character at index 4 : I
Character at index -1 : I 
Character at index -2 : S 
Character at index -3 : M 
Character at index -4 : A 
Character at index -5 : V
Hint: Use two for loops
'''
s = input("Enter the String: ")
for i in range(len(s)):
 print(f"Character at index {i} : {s[i]}")
for i in range(-1, -len(s)-1, -1):
 print(f"Character at index {i} : {s[i]}")
'''
Write a program to print characters at even and odd indexes without slice
0 1 2 3 4 5 6 7
Let input be R a m a R a o
odd = '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even = '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'
1) What action to be made when index is even ? --->
Concatenate the character to even object
2) What action to be made when index is odd ? --->
Concatenate the characeter to odd object
3) Hint: Use single for loop
'''
s = input("Enter the String: ")
even = ""
odd = ""
for i in range(len(s)):
 if i % 2 == 0: 
 even += s[i]
 else: 
 odd += s[i]
print("Even index characters:", even)
print("Odd index characters:", odd)
'''
Let input be A 4 B 3 C 2 $ 5
 0 1 2 3 4 5 6 7
What is the output ? ---> AAAABBBCC$$$$$
1) What is the result of 'A' * 4 ? ---> 'AAAA'
2) i a[i] a[i + 1] out
 -------------------------------------------------------
 ''
 0 'A' '4' '' + 'A' * 4 = 'AAAA'
2 'B' '3' 'AAAA' + 'B' * 3 = 'AAAA' + 'BBB' = 'AAAABBB'
4 'C' '2' 'AAAABBB' + 'C' * 2 = 'AAAABBB' + 'CC' = 'AAAABBBCC'
6 '$' '5' 'AAAABBBCC' + '$' * 5 = 'AAAABBBCC' + '$$$$$' = 'AAAABBBCC$$$$$'
 -------------------------------------------------------
What is the difference between a[i] and a[i + 1] ? --->
a[i] is ith char of string and a[i + 1] is (i + 
1)th char of string
'''
s = input("Enter the String: ")
string = ""
for i in range(0, len(s), 2):
 string += s[i] * int(s[i+1])
print(string) 
'''
Write a program to merge two strings to form a new string
1) Let inputs be HYD and VAMSI
 What is the output ? ---> HVYADMSI
 0 1 2
a ---> H Y D
 0 1 2 3 4
b ---> V A M S I
i a[i] b[i] c
--------------------------------------------------------
 ''
0 'H' 'V' '' + 'H' + 'V' = 'HV'
1 'Y' 'A' 'HV' + 'Y' + 'A' = 'HVYA'
2 'D' 'M' 'HVYA' + 'D' + 'M' = 'HVYADM'
--------------------------------------------------------
Concatenate remainging characters of the other string to object 'c'
What is the final result ? ---> 'HVYADMSI'
Hint: Use single while loop and slice
'''
# Take two input strings
a = input("Enter first string: ") # Example: HYD
b = input("Enter second string: ") # Example: VAMSI
c = ""
i = 0
while i < len(a) and i < len(b):
 c += a[i] + b[i]
 i += 1
c += a[i:] + b[i:]
print("Merged string:", c)
'''
Write a program to remove duplicate characters of the string without using set
1) Let input be RAMA RAO
 What is the output ? ---> RAM<space>O
2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'
3) What action to be made if the character is not in out object ? --->
Concatenate the character to out object
4) What action to be made if the character is already in out object ? --->
Ignore the character
5) Hint: Use not in operator
'''
s = input("Enter the string: ")
out = ""
for ch in s:
 if ch not in out: 
 out += ch 
print(out) 
# len() function demo program (Home work)
print(len('Hyd')) # 3
print(len('Rama Rao'))# 8
print(len('9247'))#4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
print(len(3456))#error
print('Sec'. len())#error
'''
What does len(str) do ? ---> Returns number of characters in the string
''' 
# chr() function demo program
print(chr(65)) # Converts unicode value 65 to 'A'
print(chr(90))#Z
print(chr(97))#a
print(chr(122))#z
print(chr(48))#0
print(chr(57))#9
print(chr(36))#$
print(chr(32))#<space>
'''
What does chr() function do ? ---> Converts unicode value to character
'''
# ord() function demo program
print(ord('A')) # Converts 'A' to unicode value 65
print(ord('Z'))#90
print(ord('a'))#97
print(ord('z'))#122
print(ord('0'))#48
print(ord('9'))#57
print(ord('$'))#36
print(ord(' '))#32
'''
Let input be A4M3Z5D2
What is the output ? ---> AEMPZ_DF
0 1 2 3 4 5 6 7
A 4 M 3 Z 5 D 2
 i a[i] a[i + 1] out
--------------------------------------------------------------------------------
 ''
 0 'A' '4' '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE'
 2 'M' '3' 'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP'
 4 'Z' '5' 'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '' = 'AEMPZ'
 6 'D' '2' 'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use chr() and ord() functions
'''
s = input("Enter the string: ") # Example: A4M3Z5D2
out = ""
for i in range(0, len(s), 2):
 ch = s[i]
 shift = int(s[i+1])
 out += ch + chr(ord(ch) + shift)
print(out)
