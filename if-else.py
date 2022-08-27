#conditions

#equals: a == b
#not Equals: a != b
#less than: a < b
#less than or equal to: a <= b
#greater than: a > b
#greater than or equal to: a >= b

a = int(input("enter value a: "))
b = int(input("enter value b: "))

#1 normal
#if
if a > b:
    print(a, "is greater then",b)
#elif (else if)
elif a < b:
    print(a, "is less then",b)
#else
else:
     print("the numbers are equal")

#2 short hand
#if
if a > b: print(a, "is greater then",b)
#elif (else if)
elif a < b: print(a, "is less then",b)
#else
else: print("the numbers are equal")

#and, or
if a > b and b > 0: pass #pass statement to avoid getting an error
if a > b or b > 0: pass

#nest
if a > 10:
    if a > b:
        print(a)
    else: 
        print(b)