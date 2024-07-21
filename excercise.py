#Q1 Return number of digits in number
def num(number):
    return len(str(number))
print(num(1204983))
    
#Q1a even odd function:
def evenodd(x):
    if x%2 == 0:
        return "even"
    else:
        return "odd"

print(evenodd(235098))

#Q2 return number of words in a sentence:
def words(stringinput):
    a = stringinput.split()
    return len(a)

print(words("asd fa dgfagfa f adfa sdf ad ag"))

#Q2a return number of letters in a sentence:
def numlet(stringinput):
    return len(list(stringinput))

print(numlet("My name is Vibhav"))

#Q3 Tables: takes m, n and multiplies them:
def tables(m, n):
    for i in range(1, n+1):
        #print(f"{m}x{i}={m*i}")
        a = f"{m}x{i}={m*i}"
        return a

print(tables(5, 20))

#Q4
#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20
#etc..........

def doubletriple(n):
    a = [1, 2, 3, 4]
    aa = []
    for i in range(1, n+1):
        for j in range(0, (len(a))):
            aa.append(a[j]*i)
        print(str(aa))
        aa = []
        print("\n")

print(doubletriple(10))

def doubletriple2(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{j*i}", end=" ")
        print()
    print()

print(doubletriple2(10))

#Q5 Fizzbizz write a function fizzbizz that takes n as an input and if it is a multiple of three it prints fizz, multiple of 5 print bizz, multiple of 15 fizzbizz
def fizzbizz(n):
    for i in range(1, n+1):
        if i%15 == 0:
            print('fizzbizz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('bizz')
        else:
            print(f'{i}')

print(fizzbizz(15))

#Q6 write a function that returns the largest number in the list of numbers
'''
def biggest(lst):
    lst.sort()
    return lst[-1]

print(biggest([4, 5, 6, 45, 35, 7, 4568, 345, 1345, 245, 36, 26, 2346]))

[1234, 234, 234, 6, 7]
[1234, 234], [6, 7]
[1234] [234] [6] [7]
'''

def biggestn(n):
    biggest = n[0]
    for i in range(1, len(n)):
        if n[i] > biggest:
            biggest = n[i]
    return biggest
print(biggestn([4, 5, 6, 45, 35, 7, 4568, 345, 1345, 245, 36, 26, 2346]))

#Q7 biggest2, returns largest 2:
def biggest2(n):
    biggest = n[0]
    for i in range(1, len(n)):
        if n[i] > biggest:
            biggest = n[i]
    n.remove(biggest)
    big = n[0]
    for i in range(1, len(n)):
        if n[i] > big:
            big = n[i]
    return f'{biggest}, {big}'
print(biggest2([4, 5, 6, 45, 35, 7, 4568, 345, 1345, 245, 36, 26, 2346]))
'''
#Q8 Panagram:
yn = y
alphabet = [a, b, c...]
phrase = 'today is monday'
a = list(phrase)
for i in alphabet:
    for j in a:
        if alphabet[i] == a[j]

def panagram(s):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    s = s.lower()
    phrase = list(s)
    for i in phrase:
        if phrase[i] == " ":
            phrase.remove(" ")
    if len(phrase) > 26:
        return "Not a Panagram"
    else:

        for j in phrase:
            for k in alphabet: 
                if phrase[j] == alphabet[k]:
                    x = alphabet[k]
                    alphabet.pop(x)    
        '''
def panagram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s.lower():
            return False
    return True
print(panagram("today is monday"))
print(panagram("the quick brown fox jumps over the lazy dog"))
