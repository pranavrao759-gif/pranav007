import math as m
import statistics as s
import random as r

x=0
def add(a,b):
    return a+b
def subtract(a,b):
    if b>a:
        return b-a
    else:
        return a-b
def product(a,b):
    return a*b
def quotient(a,b):
    if b==0:
        print('division by zero is not defined')
    else:
        return a/b
def remainder(a,b):
    if b==0:
        print('division by zero is not defined')
    else:
        return a%b
def expo(a,b):
    return m.pow(a,b)
def sqrt(a):
    if a<0:
        print('square root of negative number is not defined ')
    else:
        return m.sqrt(a)
def cbrt(a):
    if a>=0:
        return a**(1/3)
    else:
        return -(-a)**(1/3)
    print('cube root = ',x)
def percent(a,b):
    if b==0:
        print('divison by zero is not defined ')
    else:
        return (a/b)*100
def mean(s):
    return s.mean(d)
def median(s):
    return s.median(d)
def mode(s):
    return s.mode(d)
def sin(a):
    return m.sin(m.radians(a))
def cos(a):
    return m.cos(m.radians(a))
def tan(a):
    if a%90==0:
        print('Invalid entry.For multiples of 90 degree tangent function is not defined ')
    else:
        return m.tan(m.radians(a))
def cosec(a):        
    if a%180==0:
        print('Invalid entry.For multiples of 180 degree cosecant function is not defined ')
    else:
        return 1/(m.sin(m.radians(a)))
def sec(a):
    if a%90==0:
        print('Invalid entry.For multiples of 90 degree secant function is not defined ')
    else:
        return 1/(m.cos(m.radians(a)))
def cot(a):
    if a%180==0:
        print('Invalid entry.For multiples of 180 degree cotangent function is not defined ')
    else:
        return 1/(m.tan(m.radians(a)))
def log10(a):
    if a==0:
        print('logarithm to the base 10 of 0 is not defined')
    else:
        return m.log10(a)
def fact(a):
    if a<0:
        print('factorial of negative number is not defined')
    else:
        return m.factorial(a)
def hcf(a,b):
    if a<0 or b<0:
        print('GCD of negative number is not defined')
    else:
        return m.gcd(a,b)
def lcm(a,b):
    if a<0 or b<0:
        print('LCM of negative number is not defined')
    else:
        l=m.gcd(a,b)
        return (a*b)/l
def sininv(a):
    if a<-1 or a>1:
        print('Invalid entry.Enter the value in the range [-1,1] ')
    else:
        b=m.asin(a)
        return m.degrees(b)
def cosinv(a):
    if a<-1 or a>1:
        print('Invalid entry.Enter the value in the range [-1,1] ')
    else:
        b=m.acos(a)
        return m.degrees(b)
def taninv(a):
        b=m.atan(a)
        return m.degrees(b)
def cosecinv(a):
    if a>=1 or a<=-1:
        b=m.asin(1/a)
        return m.degrees(b)
    else:
        print('Invalid entry.Enter the value which is <=-1 or >=1')
def secinv(a):
    if a>=1 or a<=-1:
        b=m.acos(1/a)
        return m.degrees(b)
    else:
        print('Invalid entry.Enter the value which is <=-1 or >=1')
def cotinv(a):
    if a==0:
        print('cot inverse(x)= 90.0°')
    else:
        b=m.atan(1/a)
        return m.degrees(b)
def password(length):
    z=''
    a=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','L','K','J','H','G','F','D','S','A','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','-','=','[',']',';',',','.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','"',':','>','?','<',]
    for i in range(0,length):
        s=r.choice(a)
        z=z+s
    print('password :',z)

    
def counter():
    txt=input('Enter the lines of text : ')
    alp=dig=space=s_char=words=0
    for ch in txt:
        if ch.isalpha():
            alp+=1
        elif ch.isdigit():
            dig+=1
        elif ch.isspace():
            space+=1
        else:
            s_char+=1
    words=len(txt.split())
    char=len(txt)
    print('Total number of characters in the text = ',char) 
    print('Total number of digits in the text = ',dig)
    print('Total number of space in the text = ',space)
    print('Total number of alphabets in the text = ',alp)
    print('Total number of special characters in the text = ',s_char)
    print('Total number of words in the text = ',words) 


                    
