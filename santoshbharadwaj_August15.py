
isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   Truet
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha()) #false
print('Hyd$'  . isalpha())#false
print('9247'  .  isalpha())#false
print('+-$'    .  isalpha())#false
print('A2#'  .   isalpha())#false
print(''  .  isalpha())#false
print(' '  .  isalpha())#false


# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())#false
print('Hyd' . isdigit())#false
print('+-$' . isdigit())#false
print('A2#' . isdigit())#false
print('' . isdigit())#false
print(' ' . isdigit())#false
print(9247 . isdigit())#error


# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#true
print('+-$' . isupper())#false
print('HYD123' . isupper())#true
print('HYD+-$' . isupper())#true
print('' . isupper())#false

 islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())# true
print('+-$' . islower())#false
print('hyd+-$' . islower())#true
print('abc123' . islower())#true
print('' . islower())#false
print('a2#' . islower())#true



# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())#false
print('hyd' . isalnum())#true
print('hYd' . isalnum())#true
print('9247' . isalnum())#true
print('' . isalnum())#false
print('A7g9'  . isalnum())#true



# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())#false
print('\n' . isspace())# true
print('\n  $\t' . isspace())#false
print('\t' . isspace())#true
print('' . isspace())#false
print(' ' . isspace())#true

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))# a  :  25  b  :  10.8 c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a  :  25  b  :  10.8 c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a  :  Hyd b  :  10.8 c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a  :  Hyd b  :  Hyd  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a:Hyd b:Hyd c:Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a:Hyd b:10.8c:25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  25 b:25 c:25





'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''


progrm:


ch = input("Enter any single character: ")

if ch.isalnum():  
    print("Alphanumeric character")

    if ch.isalpha():  # Alphabet
        print("Alphabet character")
        if ch.isupper():
            print("Upper case alphabet")
        else:
            print("Lower case alphabet")
    elif ch.isdigit():
        print("Digit character")

elif ch.isspace():  
    print("White space")

else:  # Special character
    print("Special character")


'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'
     2       'y'             'd' + 'y' = 'dy'
     3       'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''

program:


s = input("Enter a string: ")
rev = ""

for i in range(1, len(s) + 1):
    rev += s[-i]   
print("Reversed string:", rev)



Enter  any  string : Rama Rao
Reverse  String :   oaR amaR


s = input("Enter any string: ")
rev = ""
for i in range(1, len(s) + 1):
    rev += s[-i]
print("Reverse String:", rev)
'''



Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
   1        'city'         '' + 'city' + ' '=  'city '
   2        'green'     'city ' + 'green' + ' ' = 'city green '
   3        'is'            'city green ' + 'is' + ' ' =  'city green is '
   4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''

s = input("Enter any sentence: ")

b = s.split() 

c = ""
for i in range(1, len(b) + 1):
    c += b[-i] + " "  

print("Reversed order of words:", c.strip())





'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''


s = input("Enter any sentence: ")
words = s.split()
for word in words:
    print(word[::-1], end=" ")


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''


s = input("Enter a string: ")
sorted_chars = sorted(s) 
result = "".join(sorted_chars)
print("Sorted string:", result)

'''




Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''



s = input("Enter a string: ")
sorted_str = sorted(s)
alpha = ""
digit = ""
for ch in sorted_str:
    if ch.isalpha():     
        alpha += ch
    elif ch.isdigit():  
        digit += ch
result = alpha + digit
print("Sorted string:", result)




'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

while (index := a.find('is', (index + 1) if 'index' in locals() else 0)) != -1:
    print(index)

print('End')



'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a.index('is') 
    while True:
        print(index)
        index = a.index('is', index + 1
except ValueError:
      print('End')


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->   Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  --->  Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  --->  +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index != -1:
   print(index)
   index = a.rfind('is', 0, index)
print('End')



'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  founda = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is') 
    while True:
        print(index)
        index = a.rindex('is', 0, index) 
except ValueError: 
    print('End')



#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48))
print(a . count('was'))





print(a.count('is'))          # 4 → total times 'is' appears in the string
print(a.count('is', 19, 48))  # count 'is' between index 19 and 47
print(a.count('was'))         # 0 → 'was' not found

'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->



#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3

'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''

s = input("Enter a string: ")
first_char = s[0]
result = first_char + s[1:].replace(first_char, '*')
print(result)


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))-->['15':'6':'48']
print(a)--> 15:36:48


# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))---->['Hyd\nis', 'green\tcity']
print(a . split())--->['Hyd', 'is', 'green', 'city']
print(a . split('green'))-->['Hyd\nis ', '\tcity']
print(a . split(''))--->eeror empty string


Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1


'''


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())--->['Hyd', 'is', 'green', 'city']
print(a . split(' '))--->['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))--->['www', 'gmail', 'com']


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''


expr = input("Enter an expression with + : ")
parts = expr.split('+')




#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))---->15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))---------->Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))------->10,20,25,15,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))---->www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))---->error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))--->sankarDayalsarma
g = range(5)
print('-' . join(g))---->error



# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))--->true
print(a . endswith('town'))---->false
print(a . endswith('green' , 3 , 12))------>true
print(a . endswith('green' , 3 , 13))---->false
print(a . endswith(' ' , 3 , 13))---->true


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''



word = input("Enter a string: ")
if len(word) < 3:
elif word.endswith("ing"):
result = word + "ly"
else:
 result = word + "ing"
print(result)
