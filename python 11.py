##a = int(input("enter any number  between >=0 and <=9999 "))
##c = a%10
##b = a%100
##d = b//10
##e = a//1000
##f = (a%1000)//100
##print(e)
##print(f)
##print(d)
##print(c)
##print(e ,"+", f ,"+", d ,"+", c, "=", e + f + d + c)

##a  = input("enter name of 1st pokemon ")
##b  = float(input("enter x coordinate of pokemon 1 "))
##c  = float(input("input y coordinate of pokemon 1 "))
##d  = input("enter name of 2nd pokemon ")
##e  = float(input("enter x coordinate of pokemon 2 "))
##f  = float(input("enter y coordinate of pokemon 2 "))
##g  = ((e-b)**2 + (f-c)**2)**0.5
##print ("distance between pokemon" , a , " and " , d , "is" , g)
##h = round (g,2)
##print(h)

##a = float(input("enter the length of rectangle 1 " ))
##b = float(input("enter the breadth of rectangle 1 "))
##c = float(input("enter the length of rectangle 2 "))
##d = float(input("enter the breadth of rectangle 2 "))
##area1 = a*b
##print(area1)
##area2 = c*d
##print(area2)
##
##if area1>area2:
##    print("rectangle 1 is bigger")
##elif area1 == area2:
##    print("rectangle 1 and rectangle 2 have same area")
##else:
##    print("area of rectangle 2 is bigger then rectangle 1")
##
##if a==b:
##    print("1st rectangle is a square")
##if c==d:
##    print("2nd rectangle is a square")

##a = float(input("enter coordinate x1 "))
##d = float(input("enter coordinate y1 "))
##b = float(input("enter coordinate x2 "))
##e = float(input("enter coordinate y2 "))
##c = float(input("enter coordinate x3 "))
##f = float(input("enter coordinate y3 "))
##dist1 = ((b-a)**2 + (e-d)**2)**0.5
##h = round(dist1 , 2)
##print(h)
##dist2 = ((c-b)**2 + (f-e)**2)**0.5
##i = round(dist2,2)
##print(i)
##dist3 = ((c-a)**2 + (f-d)**2)**0.5
##j = round(dist3 ,2)
##print(j)
##
##if h+i > j and i+j>h and j+h>i:
##    print("it is a valid triangle")
##else:
##    print("it is an invalid triangle")
##
##
##if h == i and i == j and j ==h:
##    print("it is an equilateral triangle")
##elif h == i or i == j or j==h:
##    print("it is a isocscles traingle")
##else:
##    print("it is a scalene triangle")

a = int(input("DD "))
b = int(input("MM "))

c = int(input("YYYY "))
MM = int(input("enter number HERE"))
x = int(a +b + c )
d = input("enter the start year of program ")
f = int(input("year of starting program "))
e = input("enter birth date DDMMYYYY ")
if 1 == MM:
    print ( "JAN")
elif 2 == MM:
    print ( "FEB")
elif 3 ==MM:
    print("MARCH")
elif 4 ==MM:
    print( "APRIL")
elif 5 ==MM:
    print("MAY")
elif 6 == MM:
    print( "JUNE")
elif 7 == MM:
    print( "JULY")
elif 8 == MM:
    print("AUGUST")
elif 9 == MM:
    print( "SEPTEMBER")
elif 10 ==MM:
    print("OCTOBER")
elif 11 == MM:
    print("NOVEMBER")
elif 12 == MM:
    print("DECEMBER")

print("the contestant was born on",a,"month" , MM , "year" , c)
if c - f >21:
    print("contestant is eligible for program")
else:
    print("contestant is ineligible for program")
































    
