# Say "Hello, World!" With Python

first_string = "Hello, World!"
print(first_string)


# Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



num = int(input())
if num %2 != 0:
    print ("Weird")
else:
    if num >= 2 and num <= 5:
        print ("Not Weird")
    if num >=6 and num <= 20:
        print("Weird")
    if num > 20:
        print ("Not Weird")


# Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
sum = a + b
dif = a - b
prod = a * b

print (sum)
print(dif)
print(prod)

# Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

int_div = a // b
flo_div = a / b

print(int_div)
print(flo_div)


# Loops

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print ( i**2)


# Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    if year % 100 == 0:  
        return False 
    if year % 4 == 0:
        return True
    else:
        return False



year = int(input())
print(is_leap(year))

# Print Function

if __name__ == '__main__':
    n = int(input())

for i in range(1, n+1):
    print (i, end="")
    

# List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

final = [[i, j, k]
    for i in range (x + 1)
    for j in range (y + 1)
    for k in range (z + 1)
         if  i + j + k !=n]
print (final)


# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
massimo = max(arr)
nuova_lista = []

for i in range(0, len(arr)):
    if arr[i] != massimo:
        nuova_lista.append(arr[i])   # inserisce i valori che sono != da max all'interno di nuova_lista che e vuota

runner_up = max(nuova_lista)

print(runner_up)
        
    
# Nested Lists

if __name__ == '__main__':
    student =[]
    for _ in range(int(input())):
        name = (input())
        score = (float(input()))
        student.append ([name, score])
        
grades =[]
    
for i in range (len(student)):
    if student [i][1] not in grades: # 1 perche prende score
        grades.append(student[i][1])
        
grades.sort()
second_lowest = grades[1]
        
final_names = []
        
for i in range (len(student)):
    if student [i][1] == second_lowest:
        final_names.append(student[i][0]) #0 perche prende name
final_names.sort() 
        
for name in final_names:
    print(name)
        
            
# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {} # dictionary
    for _ in range(n):
        name, *line = input().split() #nome
        scores = list(map(float, line)) #voto
        student_marks[name] = score # lista con nome:[voto1, voto2, voto3]
    query_name = input()

for name in student_marks[]:

# sWAP cASE

def swap_case(s):
    return s.swapcase()
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
  
# String Split and Join


def split_and_join(line):
    # write your code here
    
    parole = line.split(" ")
    return "-".join(parole)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print ("Hello", first_name, last_name + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Mutations

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string

def count_substring(string, sub_string):
    count = 0
    for i in range (len(string) - len(sub_string)+1):
        trovato = True
        
        for j in range(len(sub_string)):
            if string[j + i ] != sub_string[j]:
                trovato = False
                break
        if trovato:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# String Validators

if __name__ == '__main__':
    s = input()

print (any (c.isalnum() for c in s))
print (any (c.isalpha() for c in s))
print (any (c.isdigit() for c in s))
print (any (c.islower() for c in s))
print (any (c.isupper() for c in s))


# Text Alignment

# Enter your code here. Read input from STDIN. Print output to STDOUT

thickness = int(input()) 
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Text Wrap

import textwrap

def wrap(string, max_width):
    result = []
    for i in range (0, len(string), max_width):
        result.append (string[i:i + max_width])
    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    
    for i in range(size):
        left = alphabet [size -1:i:-1] #prende le lettere all'indietro
        right = alphabet [i:size] #prende le lettere avanti
        row = "-".join (left + right)
        lines.append (row.center(4* size -3, "-"))
        
    lines = lines[::-1]
    
    print("\n".join(lines + lines[-2::-1]))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        result.append(word.capitalize())
    
    return " ".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# The Minion Game

def minion_game(string):
    # your code goes here
    vowels = ("AEIOU")
    Kevin = 0 #vowels
    Stuart = 0 #consonant
    
    for i in range (len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i 
        else:
            Stuart += len(string) - i
    if Kevin > Stuart:
        print ("Kevin", Kevin)
    elif Stuart > Kevin:
        print ("Stuart", Stuart)
    else:
        print ("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

# Introduction to Sets

def average(array):
    # your code goes here
    heights = set(arr)
    average = sum(heights) / len(heights)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int, input().split()))

N = int(input())
b = set(map(int, input().split()))

result = a.symmetric_difference(b)

for number in sorted(result):
    print(number)

# No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT


n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for number in array:
    if number in A:
        happiness += 1
    elif number in B:
        happiness -= 1

print ( happiness)

# Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set()

for i in range(n):
    country = input().strip()
    countries.add(country)
    
print(len(countries))


# Set .discard(), .remove() & .pop()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    command = input().split()

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))


# Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

students = english.union(french)

print(len(students))


# Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
English = set(map(int, input().split()))

m = int(input())
French = set(map(int, input().split()))

print ( len(English.symmetric_difference(French)))

# Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation, length = input().split()
    other = set(map(int, input().split()))

    if operation == "update":
        A.update(other)
    elif operation == "intersection_update":
        A.intersection_update(other)
    elif operation == "difference_update":
        A.difference_update(other)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other)

print(sum(A))

# The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
room = list(map(int, input().split()))

count = {}

for i in room:
    if i not in count:
        count[i] = 1
    else:
        count[i] +=1
        
for i in count:
    if count[i] == 1:
        print(i)
        break

# Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())

for _ in range(test):
    n = int (input())
    A= set(map(int, input().split()))
    
    m = int(input())
    B = set(map(int, input().split()))
    
    result = True
    
    for i in A:
        if i not in B:
            result = False

    print(result)        
    

# Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    B = set(map(int, input().split()))

    if not A > B:
        result = False

print(result)

# Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = max(candles)
    return candles.count(tallest)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()






