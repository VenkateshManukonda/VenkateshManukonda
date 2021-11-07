#atleast one digit and char
'''
word= input('Enter a word:')
if word.isalpha() or word.isdigit():
  print("false")
else:


def ischarnum(str):
  check_1= False
  check_2= False
  for i in str:
    if i.isalpha():
      check_1= True
    if i.isdigit():
      check_2= True
  return check_1 and check_2

word=input("Enter a word:")
print(ischarnum(word))


#1/11/21
#condition statements

#1. for multiple conditions elif block is used

a= int(input("enter a number:"))
if a>0:
  print("greater digit")
elif a<0:
  print("_ve digit")
else:
  print("number is zero")


#2. Factor check of 3,7,11
value=int(input("Factor check value:"))
if value%3==0:
  print("factor of 3")
if value%7==0:
  print("factor of 7")
if value%11==0:
  print("factor of 11")
else:
  print("none")


#3. Read keyboard input based on cond

digit=int(input("enter a numb.:"))
if digit%2==0:
  print(digit**2)
else:
  if digit%5==0:
    print(digit**3)
  else:
    print(digit*10)



#4. Insurance planning

driver=input("Enter your maritial status:")
gender=input("Enter your gender:")
age=int(input("Enter your age:"))
if driver=='married':
  print("insurance issued")
elif driver=='unmarried' and gender== 'm' and age>=30:
  print("insurance issued")

elif driver=='unmarried' and gender== 'f' and age>=25:
  print("insurance issued")

else:
  print("Insurance not issued")



#check for palindrome

word=input("Enter a word to check:\n")
print(word==word[::-1])


#xhexk for number of vowels

word=input("enter the word:")
v=0
for x in word:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'  ):
        v=v+1
print("No. of vowels",v)

dictionary={"key":"value","paani":"water","aag":"fire",}
print(dictionary["aag"])

a=(2,4,5,6,78)
print(a.index(78))



def factorial(n):
	if n == 0 or n == 1 :
		return 1
	else:
		return n*factorial(n-1)

fact=int(input("enter a val"))
print(factorial(fact))

#Write a program to find out whether a student is pass or fail if it requires a total of 40% and at
# least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

#marks=int(input("enter your marks:"))

x,y,z=(input("Marks enter karo:")).split(',')
x=int(x)
y=int(y)
z=int(z)
if x and y and z >=33 and ((x+y+z)/3)>=40:
    print("Pass")
else:
    print("You are failed")
'''




