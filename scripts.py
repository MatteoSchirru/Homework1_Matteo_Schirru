#Hello, World!
if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 > 0:
    print("Weird")

if n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")

if n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")

if n % 2 == 0 and n > 20:
    print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a*b)


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    if n > 0:
        for i in range(n):
            print(i**2)

#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
        leap = True
    else:
        leap = False    
    
    return leap

year = int(input())

#Print Function
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep='')

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
list_elements = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(list_elements)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
maximum = -100
for score in arr:
    if score > maximum:
        maximum = score

runner_up = -100
for score in arr:
    if score > runner_up and score != maximum:
        runner_up = score  
 
print(runner_up)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

marks = student_marks[query_name]
avg= sum(marks) / len(marks)
print(f"{avg:.2f}")



#Lists
if __name__ == '__main__':
    N = int(input())
lista = []
    
for _ in range(N):
    istruzione = input().split()
    comando = istruzione[0]
        
    if comando == "insert":
        lista.insert(int(istruzione[1]), int(istruzione[2]))
    elif comando == "print":
        print(lista)
    elif comando == "remove":
        lista.remove(int(istruzione[1]))
    elif comando == "append":
        lista.append(int(istruzione[1]))
    elif comando == "sort":
        lista.sort()
    elif comando == "pop":
        lista.pop()
    elif comando == "reverse":
        lista.reverse()


#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    print(hash(t))

#sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':

#String Split and Join
def split_and_join(line):
    s = line.split(" ")
    s = "-".join(s)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':

#Mutations
def mutate_string(string, position, character):
    lista_caratteri = list(string)
    lista_caratteri[position] = character
    return ''.join(lista_caratteri)

if __name__ == '__main__':

#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':


#String Validators
if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
if __name__ == '__main__':

#Capitalize!
def solve(s):
    words = s.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
if __name__ == '__main__':

#String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
if __name__ == '__main__':


#Birthday Cake Candles
import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
