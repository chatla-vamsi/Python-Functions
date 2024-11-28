#to print len without using len()
'''
def len():
    return
a=input()
c=0
for i in a:
    c+=1
print(c)


def length(a):
    c=0
    for i in a:
        c+=1
    print(c)
n=input()
length(n)
'''
#global variable
'''
a=10
def f():
    print(a,'inside')
f()
print(a,'outside')
output:
10
10
'''
#local variable
'''
a=10
def f():
    a=20
    print(a,'inside')
f()
print(a)
output:
20 inside
10
'''
#convert local to global
'''
a=10
def f1():
    global a
    a=20
    print(a)
f1()
print(a)
output:
    20
    20
'''
#return
'''
a=10
def f1():
    a=20
    return a
print(f1())
output: 20
'''

#addtion,mul
'''
def operation(a,b):
    return a+b,a*b
print(operation(10,20)) #(30, 200)

a=10
def f1():
    a=20
    b=a+a
    print(b,'inside')
    return b
print(f1(),'outside')
'''



#nonlocal variable
'''
1.
def f1():
    n=100
    def f2():
        n=200
        print(n,'inside')
    f2()
    print(n,'outside')
f1()
output:
200 inside
100 outside
'''

#convert 2nd function to global
'''
def f1():
    n=100
    def f2():
        nonlocal n
        n=200
        print(n,'inside')
    f2()
    print(n,'outside')
f1()

output:
200 inside
200 outside
'''

#types of arguments
'''
1.positional arguments
2.keyword arguments
3.default arguments
4.

2.keyword
----------

def fun(name,age):
    print(name,age)
fun(age=23,name='neha')


output;neha 23
'''
#combination of positional ang keyword arguments
#only positional argument
'''
in this type we use a special symbol / where the arguments before the / must be positional
and the argumenrts after the / can be positional or keyword
syntax:-
def f1(arg1,arg2,/,arg3):
    pass
f1(data1,data2,data3)
EX:-
def f1(name,age,/,id):
    print(name,age)
f1('pavan',21,2)
f1('ram',30,id=4)

output:
pavan 21
ram 30
'''
#only keyword argument
'''
in this type we use the special symbol * where the arguments after the star mus tbe keyword
argument and the arguments before can be postional or keyword.

def f1(arg1,arg2,*,arg3):
    pass
f1(data1,data2,arg3=data3)
f1(arg1=data1,arg2=data2,arg3=data3)



def f1(a,b,*,c,d):
    print(a,b,c,d)
f1(a=10,b=20,c=30,d=23)
f1(10,20,c=30,d=23)
f1(10,b=20,c=30,d=45)

output:
10 20 30 23
10 20 30 23
10 20 30 45
'''

#variable position argument
'''

def f1(*args):
    print(args)
f1(3,4,5)
f1('hwllo','kai')

output:
(3, 4, 5)
('hwllo', 'kai')

'''
#variable keyword argument
'''
def f1(**args):
    print(args)
f1(a=34,b=3.4,c=False)
output:
{'a': 34, 'b': 3.4, 'c': False}
'''
'''
def f1(s,*args,**kargs):
    print('\n',s,'\n',args,'\n',kargs)
f1(3.4,4,(3,4),c=False,d='python',e=[False,True])

output:
3.4 
 (4, (3, 4)) 
 {'c': False, 'd': 'python', 'e': [False, True]}
'''

#default arguments
'''
def f1(a=2,b=10):
    return(a**2,b**3)
print(f1(3,5))
print(f1(4))
print(f1())

output:
(9, 125)
(16, 1000)
(4, 1000)

'''
#a function takes variable no.of positional arguments as input.how to check if
#the arguments thta are passed more than 5
'''
def f1(a=input('enter a number')):
    if(len(a)>=5):
        print("True")
    else:
        print("False")


f1()
enter a number12345
True
'''
#write a function to prite the below output
'''
def f1(s):
    a=''
    b=''
    for i in range(len(s)):
        if(i%2==0):
            a=a+s[i]
        else:
            b=b+s[i]
    print(a)
    print(b)
s=input()
f1(s)


def f1(a,b):
    if(b==0):
        print(a[1::2])
    else:
        print(a[::2])
f1('tracxn',0)
f1('tracxn',1)

'''


#Write a function to check if the number is Prime
'''
def prime(n,f=0):
    for i in range(1,n+1):
        if(n%i==0):
            f+=1
    return f==2
n=int(input())
if(prime(n)):
    print("PRIME NUMBER")
else:
    print("NOT PRIME NUMBER")


def prime(n):
    for i in range(1,n//2+1):
        if(n%i==0):
            return False
    return True
n=int(input())
if(prime(n)):
    print("PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")


def prime(n):
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
n=int(input())
if(prime(n)):
    print("PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")
'''
'''
def prime(n,m):
    for i in range(n,m+1):
        f=1
        if(i==1):
            pass
        else:
            for j in range(2,i):
                if(i%j==0):
                    f+=1
                    break
            if(f<2):
                print(i)
n=int(input())
m=int(input())
prime(n,m)
'''

#Write a method that returns the last digit of an integer.
#For example, the call of get_last_digit(3572) should return 2.
'''
def last_digit(n):
    a=str(n)
    b=a[-1]
    print(b)
n=int(input())
last_digit(n)
'''
#Make a function named tail that takes a sequence (like a list, string, or tuple)
#and a number n and returns the last n elements from the given sequence, as a list.
'''
def tail(n,m):
    a=n[m:]
    l=[]
    for i in a:
        l.append(int(i))
    print(l)
n=input().split(',')
m=int(input())
tail(n,m)
    
'''
#Write function named is_perfect_square that accepts a number and returns
#True if it's a perfect square and False if it's not.
'''
def is_perfect_square(n):
    a=n**0.5
    if(a*a==n):
        print("TRUE")
    else:
        print("FALSE")
n=int(input())
is_perfect_square(n)
'''

#Write a function which returns the sum of lengths of all the iterables
'''
def length(n):
    s=0
    for i in n:
        s+=int(i)
    print(s)
n=input()
length(n)
'''

#Python function  to check if a given number is Fibonacci number?
'''
def fibonaci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(b)
n=int(input())
fibonaci(n)
'''
##amstrong number

'''
n=int(input("Enter 6 digits number"))
b=str(n)
c=len(b)
s=0
for i in b:
    a=int(i)**c
    s+=a
if(n==s):
    print("amstrong number")
else:
    print("Not amstrong number")

#orrr

def amstrong_number(n,dup,power,sum=0):
    while n!=0:
        last_digit=n%10
        sum+=last_digit**power
        n//=10
    return dup==sum

n=int(input())
if(amstrong_number(n,n,len(str(n)))):
    print("AMSTRONG NUMBER")
else:
    print("NOT AMSTRONG NUMBER")


#or

def amstrong_number(n,power,sum=0):
    for i in str(n):
        b=int(i)**power
        sum+=b
    if(sum==n):
        print("amstrong")
    else:
        print("not")
n=int(input())
amstrong_number(n,len(str(n)))

#or


a=int(input())
n=int(input())
for i in range(a,n+1):
    b=str(i)
    c=len(b)
    s=0
    for j in range(0,c):
        s+=int(b[j])**c
    if(s==i):
        print(i)

##or

def amstrong_range(n,m):
    for i in range(n,m+1):
        a=str(i)
        b=len(a)
        s=0
        for j in range(b):
            s+=int(a[j])**b
        if(s==i):
            print(i)
n=int(input())
m=int(input())
amstrong_range(n,m))
'''
###disamstrong number 123=1**1+2**2+3**3
'''

def amstrong_number(n,dup,power,sum=0):
    while n!=0:
        last_digit=n%10
        sum+=last_digit**power
        power-=1
        n//=10
    return dup==sum

n=int(input())
if(amstrong_number(n,n,len(str(n)))):
    print("disAMSTRONG NUMBER")
else:
    print("NOT AMSTRONG NUMBER")
    

def disarium_number(n,s=0):
    for i,j in enumerate(str(n)):
        a=int(j)**(i+1)
        s+=a
    return s==n
n=int(input())
if(disarium_number(n)):
    print("DISARIUM")
else:
    print("NOT DISARIUM")

##range disarium number
def disarium_number(n,m):
    for i in range(n,m+1):
        s=0
        for j,k in enumerate(str(i)):
            a=int(k)**(j+1)
            s+=a
        if(s==i):
            print(i)
n=int(input())
m=int(input())
disarium_number(n,m)
'''
#strong number
'''
def strong_number(n,s=0):
    a=str(n)[::-1]
    for i in a:
        f=1
        for j in range(1,int(i)+1):
            f=f*j
        s+=f
    return s==n
n=int(input())
if(strong_number(n)):
    print("STRONG NUMBER")
else:
    print("NOT STRONG NUMBR")

###or

def factorial(n,f=1):
    for i in range(1,n+1):
        f*=i
    return f
def strong_number(n1,s=0):
    while n1!=0:
        rem=n1%10
        s+=factorial(rem)
        n1//=10
    return s==n2
n2=int(input())
if(strong_number(n2)):
    print("STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")

##strong number range
def strong_number_range(n,m):
    for i in range(n,m+1):
        a=str(i)[::-1]
        s=0
        for j in a:
            f=1
            for k in range(1,int(j)+1):
                f=f*k
            s+=f
        if(s==i):
            print(i)
n=int(input())
m=int(input())
strong_number_range(n,m)
'''
#repeated char using function
'''
def repeated_char(n,l=[],d={}):
    for j in n:
        l.append(int(j))
    for i in l:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    for char,count in d.items():
        if(count>1):
            print(char)
n=input().split()

repeated_char(n)
'''
#without repeated char using function
'''
def repeated_char(n,l=[],d={}):
    for j in n:
        l.append(int(j))
    for i in l:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    for char,count in d.items():
        if(count<2):
            print(char)
n=input().split()
repeated_char(n)
'''

######
'''
def pattern(n):
    for i in range(1,n+1):
        print('0 '*(n-i)+str((n-i+1)))
n=int(input())
pattern(n)
'''
'''
n=5
for i in range(1,n+1):
    print('  '*(n-i),end=' ')
    for j in range(i):
        print(chr(65+j),end=' ')
    print()
'''
####

'''
def middle(n):
    a=len(n)//2
    for i in range(1,len(n)):
        print('  '*(len(n)-i),end=' ')
        for j in range(i):
            print(n[a+j],end='')
            
        print()
n=input()
middle(n)
'''

#median using two lists
'''
def list(n,m,l=[],l1=[]):
    for i in n:
        l.append(int(i))
    for j in m:
        l1.append(int(j))
    a=sorted(l+l1)
    print(a)
    b=len(a)//2
    if(b%2==0):
        print((a[b]+a[b-1])/2)
    else:
        print(a[b])
n=input().split()   
m=input().split()
list(n,m)

output:
1 2
3 4
[1, 2, 3, 4]
2.5
'''
#if u give any char in the string it prints first half in reverse
'''
def string(n):
    a=n.index(m)
    print(n[:a][::-1]+n[a+1:])
        
n=input()
m=input()
string(n)

output:

string
i
rtsng


'''
'''

         g
        gr
       gra
      gram
     gramp
    grampr
   grampro
'''
'''
str_ = ''
input_ = 'program'
middle_index = len(input_)//2
middle_char = input_[middle_index]
print(middle_char)
for i in range(middle_index, len(input_)):
    str_ = str_ + input_[i]
    print(f'{str_:>10}')
    if i == len(input_)-1:
        for j in range(0, middle_index):
            str_ = str_ + input_[j]
            print(f'{str_:>10}')
                     



def pattern(n,str1=''):
    middle_index=len(n)//2
    middle_char=n[middle_index]
    for i in range(middle_index,len(n)):
        str1+=n[i]
        print(f'{str1:>10}')
        if(i==len(n)-1):
            for j in range(0,middle_index):
                str1+=n[j]
                print(f'{str1:>10}')
n=input()
pattern(n)

'''

#sum of single elements in a list
'''
def sum_single_elements(n,l=[],d={},s=0):
    for i in n:
        l.append(int(i))
    print(l)
    for j in l:
        if(j in d):
            d[j]+=1
        else:
            d[j]=1 
    print(d)
    for char,value in d.items():
        if(value==1):
            s+=char
    print(s)
n=input().split()
sum_single_elements(n)

'''
#if you enter a number it prints the index value and
#if the nyumber is nt present its prints[-1,-1]
#if the length the list is zero it prints[-1,-1]
'''
def position(n,l=[],l1=[]):
    for i in n:
        l.append(int(i))
    if(len(n)==0):
        print([-1,-1])
    elif(a not in l):
        print([-1,-1])
    else:
        for j in enumerate(l):
            if(j[1]==a):
                l1.append(j[0])
        print(l1)
                
n=input()
a=int(input())
position(n)


output:
123454     
4
[3, 5]
'''

#[[4,5,8,2],[3],[5],[10],[9],[4]] it adds the next element to first
'''
def add_next_element(n):
    a=n[0]
    for i in range(1,len(n)):
        a.append(n[i][0])
        b=sorted(a)
        print(b[i+1])
n=[[4,5,8,2],[3],[5],[10],[9],[4]]
add_next_element(n)
'''
#smallest common element in 2 sets
'''
def smallest_common_element(n,m):
    s=set()
    a={int(i)for i in n}
    b={int(j) for j in m}
    print(min(a.intersection(b)))
n=input()
m=input()
smallest_common_element(n,m)
'''

#a23b12c2
'''
s=input()
s1=''
l=[]
for i in s:
    if(i.isalpha()):
        s1+=' '
        l+=[i]
    else:
        s1+=i
l1=s1.split(' ')
l1.remove('')
print(''.join([c * int(num) for num,c in zip(l1,l)]))

output:
a10b5c12
aaaaaaaaaabbbbbcccccccccccc
'''
#if u give a number that equal to the sum of elements in a list
'''
l=input().split(',')#5,3,4,9,7,5
a=[]
for k in l:
    a.append(int(k))
n=int(input()) #12
p=set()
s=set()
for i in a: #[5,3,4,9,7,5]
    num=n-i
    if(num in s):
        p.add((min(i,num),max(i,num)))
    else:
        s.add(i)
for j in p:
    print(j)
'''
###############
'''
def combination_sum(n,target,l=[]):
    for i in range(1,len(n)-1):
        if(n[i-1]+n1[i]+n[i+1]==target):
            l.append((n[i-1],n[i],n[i+1]))
    print(l)
n=[10,1,2,7,6,1,5]
target=int(input())
combination_sum(n,target)


output:
13
[(10, 1, 2), (7, 6, 0)]
'''
####
'''
def combination_sum(n,target,s=set(),p=set(),l=[],d={},repeat=[]):
    for i in range(len(n)):
        a,b=n[:i],n[i:]
        for j in range(len(a)):
            for k in range(len(b)-1):
                if(a[j]+b[k]==target):
                    s.add((a[j],b[k]))
                elif(a[j]+b[k]+b[k+1]==target):
                    s.add((a[j],b[k],b[k+1]))
    print(s)
    for h in s:
        a=sorted(h)
        l.append(a)
    print(l)
    for element in l:
        if(element not in repeat):
            repeat.append(element)
    print(repeat)
n=[10,1,2,7,6,1,5]
target=int(input())
combination_sum(n,target)

output:
[[1, 7], [2, 6], [1, 2, 5], [1, 1, 6]]

'''
#####
'''
def combination_sum(n,target,s=set(),p=set(),l=[]):
    for i in range(len(n)):
        a,b=n[:i],n[i:]
        for j in range(len(a)):
            for k in range(len(b)-1):
                if(a[j]+b[k]==target):
                    s.add((a[j],b[k]))
                elif(a[j]==target):
                    s.add(a[j])
                elif(b[k]==target):
                    s.add(b[k])
                elif(a[j]+b[k]+b[k+1]==target):
                    s.add((a[j],b[k],b[k+1]))
    print(s)
#n=[10,1,2,7,6,1,5]
n=[2,5,2,1,2]
target=int(input())
combination_sum(n,target)
'''
###a12b4c10
'''
s=input()
s1=''
l=[]
for i in s:
    if(i.isalpha()):
        s1+=' '
        l+=[i]
    else:
        s1+=i
print(s1)
l1=s1.split(' ')
l1.remove('')
print(l)
print(l1)
print(''.join([c * int(num) for num,c in zip(l1,l)]))

'''

#missing number and repeated char
'''
def missing_number(n,l=[],missing=[],d={},repeated=[]):
    for i in n:
        l.append(int(i))
    a=sorted(l)
    for j in range(a[0],a[-1]+1):
        if(j not in a):
            missing.append(j)
    for k in l:
        if(k in d):
            d[k]+=1
        else:
            d[k]=1
    for char,count in d.items():
        if(count>1):
            repeated.append(char)
    print(f'missing elements:{missing} \nrepeated char:{repeated} \noutput {missing+repeated}' )
n=input().split()
missing_number(n)

output:
1 2 5 7 10 15 2 1
missing elements:[3, 4, 6, 8, 9, 11, 12, 13, 14] 
repeated char:[1, 2] 
output [3, 4, 6, 8, 9, 11, 12, 13, 14, 1, 2]
'''


#########
'''
def add_number(n,m,p):
    a=lambda v:int(v)
    b=list(map(a,n))
    c=lambda i:int(i)
    d=list(map(c,m))
    print(b,d)
    first_list=b[:p]
    second_list=d[:p]
    print(sorted(first_list+second_list))
    
n=input()
m=input()
p=int(input())
add_number(n,m,p)


output:
123000
456789
3
[1, 2, 3, 0, 0, 0] [4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6]
'''


##112223==311222
'''
n=input()
l=[]
l1=[]
l2=[]
l3=[]
d={}
d1=[]
s=set()
for i in n:
    l.append(int(i))
print(l)
for j in l:
    if(j in d):
        d[j]+=1
    else:
        d[j]=1
print(d)
b=sorted(d.values())
for k in b:
    for char,count in d.items():
        if(k==count):
            l1.append(str(char)*k)
print(l1)
for b in l1:
    if b in l2:
        pass
    else:
        l2.append(b)
print(l2)
            
for h in l2:
    for b in h:
        l3.append(int(b))
print(l3)
'''

#######
'''
#l=[1,2,3,4,5,6,7]
l=[-1,-100,3,99]
k=int(input())
for i in range(1,k+1):
    #print(l[i+1:]+l[:i])
    print(l[-i:]+l[:-i])
output:
3
[7, 1, 2, 3, 4, 5, 6]
[6, 7, 1, 2, 3, 4, 5]
[5, 6, 7, 1, 2, 3, 4]
'''



'''
n=list(input())
a=len(n)
s=''
l=[]
for i in n:
    if(a==1):
        s=s+str(int(i)+1)
        print(list(s))
    else:
        b=n[-1]
print(n[:-1]+[int(b)+1])

'''

#####
'''
n=input()
l=[]
a=len(n)
s=''
l1=[]
for i in n:
    l.append(int(i))
for j in l:
    if(a==1):
        s=s+str(j+1)
        print([int(k) for k in s])
    else:
        print(l[:-1]+[l[-1]+1])
        break


output:
1234
[1, 2, 3, 5]

9
[1, 0]

'''




#multiple highest number
'''
def multiple(n,m,l=[],l2=[]):
    a=[int(i) for i in n]
    for j in range(len(a)):
        if(m*j in a):
            l2.append(m*j)
        elif(m not in a):
            l2.append('no')
            break
    print(l2)
n=input()
m=int(input())
multiple(n,m)


output:
34567
4
[3, 4, 5, 6, 7]
4

'''

###
#if you give a number 3*2 =6 6*2=12 like that it goes
#if the ouput is not in the list you print the output
'''
def multiple(n,m,l=[],l2=[]):
    a=[int(i) for i in n]
    print(a)
    b=m*2
    for j in range(1,len(a)):
        if(b in a):
            b=b*2
    print(b)
n=input().split()
m=int(input())
multiple(n,m)

output:
5 3 6 1 12
3
[5, 3, 6, 1, 12]
24
'''
'''

n=10
def f1():
    n=100
    def f2():
        n=200
        print(n)
    f2()
    print(n)
f1()
print(n)
'''
