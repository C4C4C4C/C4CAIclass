# !/usr/bin/env python
#coding=utf-8
import random
##1
fruits = ["apple","peach","lvchee","pear","mango"]

##2
for i in fruits:
    if i == "apple":
        print("i found it!")

##3        
fruits.append("orange")
fruits.append("pinapple")
fruits.append("kiwi")

##4
fl = []
for i in fruits:
    fl.append(len(i))
    print(i,"has",len(i),"letters")

##5
def half_squared(list):
    for i in [0,len(list)-1]:
        list[i] = (list[i]**2)/2
    return list
print(half_squared([3,3])==[4.5,4.5])

##6  
score = int(input("input first number: "))
grade = ""
if score <=100 & score >=90:
    grade ="A"
    print(grade)
elif score >=60 :
    grade ="B"
    print(grade)
elif score >=0 :
        grade ="C"
        print(grade)
else:
    print("error")

##7
def revSort (a,b,c):
    if c<=b:
        if b<=a:
            a,b,c = a,b,c
        else:
            a,b,c = b,a,c
    else:        
        a,b,c = a,c,b
        if a>=b:
            a,b,c = a,b,c    
        else:
            a,b,c = b,a,c  
        if c>=b:
            a,b,c = a,c,b
    return a,b,c

##8  
def traverse(list):
    s = ""
    for i in list:
        for x in i:
            s = s +str(x)+" "
    return s

##9
l = range(1,101)  
count = 1
def f(x):
    return x**3
for i in map(f,l):
    temp = 0
    for p in range(0,len(str(i))):
        temp += int(str(i)[p])
    if temp == count:
        print(count)    
    count+=1  

##10        
x = random.randint(1,10)    
y = random.randint(1,10)     
print(x,y)
x,y = y,x
print(x,y)    
 
##11
for i in range(0,7):
    line = ""  
    if i <= 3:
        blank = 3-i
        for q in range(0,blank):
            line=line+" "
        for h in range(0,2*i+1):
            line=line+"*"          
        for p in range(0,blank):
            line=line+" "
    else:
        blank = i-3
        for q in range(0,blank):
            line=line+" "
        for h in range(0,7-2*(i-3)):
            line=line+"*"          
        for p in range(0,blank):
            line=line+" "
    print(line)

##12    
for i in range(1,7):
    for j in range(i,7):
        print(j,end = "")
    for q in range(1,i):
        print(q,end = "")
    print()  
    
##13
players = ['charles','martina','michael','florence','eli']
players1 = []
for i in players:
    players1.append(i.title())
ct = 0
for i in range(0,5):
    for j in range(i+1,6):        
        print(players1[i:j])

    
    
    
       
    