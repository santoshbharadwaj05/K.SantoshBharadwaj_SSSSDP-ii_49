'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	while  i := a . index(15 , i + 1):
		print(i)
		
except:
	print(F'15  is  found  {a . count(15)}  times ')



'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
l1= [10 , 20 , 30]
l2=[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
flag=True
ind=-1
for i in range(len(l1)):
    if l1[i] in l2[ind+1:]:
	    ind=l2.index(l1[i],ind+1)
    else:
	    flag=False
print(flag)




 # copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10 , 20 , 15 , 18]
print(a  is  b) # False
print(a  ==  b) #  True
c = a[:]
print(c) # [10 , 20 , 15 , 18]
print(a  is  c) # False
print(a  ==  c) # true
d = a
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True
print(a  ==  d) # True





'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
    ctr = 5
'''
l1=eval(input("Enter the list : "))
l2=set(l1)
c=0
for x in l2:
    if l1.count(x)>c:
        res=x
        c=l1.count(x)
        
print("mode =",res)
print("ctr =",c)




a = [[10 , 20 , 30 ,  40] ,
     [50 , 60 ,  70 , 80] ,
     [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40] , [50 , 60 ,  70 , 80] ,[90 , 100 , 110 , 120] ]
print(len(a))             # 3
print(a[0])               # [10 , 20 , 30 ,  40]
print(a[1])               # [50 , 60 ,  70 , 80]
print(a[2])               # [90 , 100 , 110 , 120]
print(a[0][2])            # 30
print(a[1][3])            # 80
print(a[2][1])            # 100





a = [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90] ]
print(a[0])        # [10 , 20]
print(a[1])        # [30 , 40 , 50]
print(a[2])        # [60 , 70 , 80 , 90]
print(len(a[0]))   # 2
print(len(a[1]))   # 3
print(len(a[2]))   # 4




a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for x in a:
    print(x)

print()
for x , y in a:
    print(x , y , sep='...')
output[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80





a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for x in a:
    print(x)

print()
for x , y , z in a:
    print(x , y , z , sep='...')

[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90





a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for x in a:
    print(x)

for x , y in a:   # ERROR
    print(x , y , sep='...')
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]




a = [[]]
print(a[0])     # []
print(a[-1])    # []




a = [[10 , 'Rama' , 1000.0] ,
     [20 , 'Sita' , 2000.0] ,
     [15 , 'Rajesh' , 3500.0] ,
     [18 , 'Kiran' , 2800.0] ,
     [5 , 'Amar' , 5000.0] ]
print(sorted(a))                # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse=True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)                        # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
