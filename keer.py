#1. Implement palindrome using iterator(for loop) and generator mechanism.
print("---------------program 1---------------")
n="12321"
s=""
for i in n:
    s=i+s
if (n==s):
    print("palindrome")
else:
    print("it is not palindrome")
    
print("---------------program 2-------------------")
# 2. Sum of 2 digits into output
# 		n1 = 1234 # int(input("Enter number1 :" ))
# 		n2 = 9999 # int(input("Enter number2 :" ))
# 		Output: 9+1 2+9 3+9 4+9 
# 		         10 + 11 + 12 + 13
# 				 46

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num1 = list(str(num1))
num2 = list(str(num2))
Out = []
n = 0
for i in num1:
    res = int(i) + int(num2[n])
    Out.append(res)
    n += 1
    continue
print(f"Sum of two digit is: {sum(Out)}")
print("----------------program 3------------------")
# 3. st = "ab@#cd!ef"
#    Reverse string considering only alphabets. Symobls should not be reversed
#    # Output: fe@#dc!ba
st = "ab@cd!ef"
st1 = st[::-1]
st1 = list(st1)
rev = ''
l = []
for i,j in enumerate(st1):
    if j.isalpha():
        l.append(j)
    else:
        l.insert(i, st[i])
rev_str = rev.join(l)
print(rev_str)
print("-------------------program 4---------------------")
#4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
dup={}
for i in some_list:
    dup[i]=some_list.count(i)
print(dup)
print("---------------program 5------------------------")
#5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
t1 = (1, 2, 3, "a", "c") 
t2 = ("b", "d", 9, 8, 7)
l1 = []
l2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in l2 and isinstance(i, int):
                l2.append(i)
                l1.append((t + i))
                break
    else:
        for i in t2:
            if i not in l2 and isinstance(i, str):
                l2.append(i)
                l1.append((t + i))
                break
print(l1)
print("----------------program 6---------------------------")
#6  #Write a Python program to remove leading zeros from an IP address.
			 # inp = "216.08.094.196"
			# o/p =  216.8.94.196

import re
inp = "216.08.094.196"
str=re.sub('\.[0]*','.',inp)
print(str)
print("-------------------program 7-------------------")
#7. l = [1, 2,[3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]

lis = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
def rec(l):
    li = []
    for i in l:
        if isinstance(i, int):
            li.append(i)
        elif isinstance(i, list):
            x = rec(i)
            li.extend(x)
    return li
print(rec(lis))

print("---------------program 8------------------")
# 8. Load sample content in text file.
#    Read data and find
#     1. No of lines in file
# 	2. No of words in each line 
# 	3. No of chars in each line
# 	4. No of vowels and consonants
# 	5. No of special chars linewise and total 
# 1. No of lines in file

with open('data.txt', 'r') as f:
    read_file = f.read()
    lines = read_file.splitlines()
    no_of_lines = len(lines)
    print("----------1. No of lines in file--------------",no_of_lines)
    
    di = dict()
    line_number = range(1, len(lines)+1)
    y = 0
    di = di.fromkeys(line_number, y)
    i = 1
    for line in lines:
        count = 0
        for char in line:
            count += 1
        di[i] = count
        i += 1
    print("----------------2. No of words in each line-----------",di)

    # No of words in each line are
    di = dict()
    no_of_words = range(1, len(lines)+1)
    y = 0
    di = di.fromkeys(line_number, y)
    i = 1
    for line in lines:
        words = line.split()
        di[i] = len(words)
        i += 1
    print("---------------3. No of chars in each line-----------------",di)

    vowels = ['a', 'e', 'i', 'o', 'u']
    vow = 0
    cons = 0
    sp_char = 0
    for i in read_file:
        if i.isalpha():
            if i.lower() in vowels:
                vow += 1
        if i.isalpha():
            if i.lower() not in vowels:
                cons += 1
        if not (i.isnumeric() or i.isalpha()):
            sp_char += 1
    print("---------------4. No of vowels and consonants---------------",vow,cons)
    print("---------------5. No of special chars linewise and total ------------",sp_char)
