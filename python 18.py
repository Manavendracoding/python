##i = 0
##while True:
##    if i == 201:
##        break
##    print(i)
##    i = i + 1


##p = "continue"
##while p=="continue" :
##    a = input(" enter your name ")
##    print(a)
##    p = input(" enter stop or continue ")



##while True:
##    
##    n = int(input(" enter any number "))
##    if n == 13 :
##        break
##    print (n)





##n = [ 3 , 4 , 6 , 7 , 2 , 5 , 11 ]
##while True:
##    p = int(input( " enter age of student "))
##    if p == (n[3]):
##        break
##    print ( p )
    
##i = 0
##while i < 100:
##    i = i + 1
##    if i == 50:
##        continue
##    print(i)
    






##i = 49
##while i < 500:
##    i = i + 1
##    if i == 200 or i == 300 or i == 400:
##        continue
##    print(i)
   




##a = int(input(" enter number 1 "))
##b = int(input(" enter number 2 "))
##c = int(input(" enter number 3 "))
####while i > a and i < b:
##    print(i)
##    if i == c:
##        continue
##    print(i)
##    
####for i in range (a,b+1,1):
####    if i==c:
####        continue
####    print(i)
   
####while a != b:
####    a = a + 1
####    if a == c:
####        continue
####    print(a)
    





##a = int(input("enter number 1 "))
##b = int(input("enter number 2 "))
##c = int(input("enter number 3 "))
##d = int(input("enter number 4 "))
##a = a - 1
##while a != b:
##    a = a + 1
##    if a == c or a == d:
##        continue
##    print(a)






##a = input("enter word 1 ")
##print(a[2:5])
##b = input("enter word 2 ")
##c = a + " " + b
##print(c)



##a = input("enter any word ")
##b = input("check for letter ")
##if b in a:
##    print("yes ")
##else:
##    print("no ")


str1 = "python is easy to learn "
str2 = "PYTHON IS EASY TO LEARN "
str3 = "Python Is Easy To Learn "
str4 = "    \n     \t    "
str5 = "1234567890"
str6 = "     python is easy to learn     "
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str2.lower())
print(str3.swapcase())
print(str1.center(100))
print(str1.ljust(100))
print(str1.rjust(100))
print(str1.center(100,"*"))
print(str1.ljust(100,"*"))
print(str1.rjust(100,"*"))
print(str1.join("++"))
print(str1.join("+++"))
x = ["cat" , "rat" , "bat" , "hat"]
y = " ".join(x)
print(y)
print(str1.replace("s","z"))
print(str1.replace("python","coding"))
print(str1.count("s"))
print(str4.isspace())
print(str1.isspace())
print(str5.isdigit())
#is methods give boolean only
print(str5.isnumeric())
print(str5.isdecimal())
print(str4.isdecimal())
print(str1.isalpha())
print(str1.isalnum())
print(str1.islower())
print(str2.isupper())
print(str3.istitle())
print(str1.startswith("p"))
print(str1.startswith("a"))
print(str1.endswith("n"))
print(str1.find("s"))
print(str1.find("z"))
print(str1.index("s"))
##print(str1.index("z"))
print(str1.rfind("s"))
print(str1.rindex("s"))
print(str6.lstrip())
print(str6.rstrip())
print(str6.strip())
print(str1.split())
print(str1.split("s"))
print(str1.split("n"))
message = """russia will attack ukraine.
It will drop bombs , and other arms aswell.
They are at War, so there will be loss of lives.
It is very dangerous."""
print(message.split())

print(message.split("\n"))
print(message.splitlines())
print(str1.partition("s"))
print(str1.rpartition("s"))
str7 = "the quick brown fox umped over the lazy dog "
print(str7)
x = str7.maketrans("abcdef", "123456")
print(str7.translate(x))
a = "burger"
b = "fries"
print("i want to eat" , a , "and" ,b)
print("i want to eat" + " " + a + " " + "and" + " " + b)
c =  "I want to eat {} and {} ".format (a , b )
print(c)
d = "i want to eat {1} and {0}".format(a , b)
print(d)
e = f"i want to eat {a} and {b} "
print(e)















 









































































