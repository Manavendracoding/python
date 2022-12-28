##colors = (" red", "orange", "black", "blue", "green")
##print(colors)
##print(type(colors))
##
##print(colors[2])
##print(len(colors))
##print(colors[1:3])
##colors[0] = "grey"

##a = ()
##print(a)
##print(type(a))
##b = tuple()
##print(b)
##print(type(b

##items = ["monday", "tuesday", "wednesday", "thursday", "friday"]
##x = tuple(items)
##print(x)
##print(type(x))
##
##y = list(x)
##print(y)
##print(type(y))

##color = ("red")
##print(color)
##print(type(color))
##
##days = ("mon","tues")
##print(days)
##print(type(days))
##
##y = ("may",)
##print(y)
##print(type(y))
##
##
##m,n,o = ("rohan","aryan","ram")
##print(m)
##print(n)
##print(o)

##names = ["sunflower","lily","daisy","rose"]
##a,b,c,d = names
##print(a)
##print(b)
##print(c)
##print(d)
##print(a,b,c,d)
##
##
##x,y,z = "the"
#print(x,y,z)

##i = input("enter your name")
##j = input("enter your surname")
##k = input("address")
##a = (i,j,k)
##print(a)
##print(type(a))

##p = int(input("number1 "))
##q = int(input("number2 "))
##r = int(input("number3 "))
##a = (p,q,r)
##print(a)
##print(type(a))

##shopping = {"watch":4000, "jeans":2800, "shirt":2900, "hanky":2800}
##print(shopping)
##print(type(shopping))
##
##print(shopping["watch"])
##
##shopping["shirt"] = 7000
##print(shopping)
##
##shopping["shoes"] = 5500
##print(shopping)

#del shopping["shirt"]
#print(shopping)

##x = {}
##print(x)
##print(type(x))
##
##y = dict()
##print(y)
##print(type(y))


##week = {"yesterday":"friday", "today":"saturday", "tomorrow":"sunday"}
##print(week)
##print(type(week))
##print(week.keys())
##
##
##print(week.values())
##
##print(week.items())

##print(sorted(week.keys()))
##
##print(sorted(week.values()))
##print(sorted(week))
##print(sorted(week.keys(), reverse = True))
##
##print(sorted(week.values(), reverse = True))
##print(sorted(week.keys(), key = len))
##
##print(sorted(week.values(), key = len, reverse = True))

#print(week["dayafter"])

##print(week.get("dayafter"))
##print(week.get("tomorrow"))
##print(week.get("dayafter", 0))
##
##print(week.pop("today"))
##print(week)
##x = week.copy()
##print(x)
##y = x.clear()
##print(y)
##print(week)
##
##week.setdefault("everyday","january")
##print(week)
##week.setdefault("everyday","holiday")
##print(week)

##a = input("name of friend one ")
##b = input("name of friend two ")
##c = input("name of friend three ")
##d = int(input("age of friend one "))
##e = int(input("age of friend two "))
##f = int(input("age of friend three "))
##g = {a:d, b:e, c:f}
##print(g)


##b = {"jan":"1stmonth","feb":"2ndmonth","march":"thirdmonth"}
##c = {"add1":"b401","add2":"b402","add3":"b403"}
##c.update(b)
##print(c)
##
##a = dict.fromkeys([1,2,3,4,5])
##print(a)
##b = dict.fromkeys(("bed", "pillow", "tablelamp"),"home")
##print(b)
##
##print("bed" in b)
##print("bed" not in b)


##j = {"alpha", "bravo", "charlie","alpha"}
##print(j)
##print(type(j))
##print(len(j))
##k,m,n = ("alpha","bravo","charlie")
##print(k)
##print(m)
##print(n)
##x = set()
##print(x)
##print(type(x))

##L = {"mon", "tues", "wed"}
##print(L)
##L.add("fri")
##print(L)
##
##m = {"thurs", "sat", "sun"}
##L.update(m)
##print(L)
##
##week = L.copy()
##print(week)
##
##L.clear()
##print(L)
##
##week.discard("tues")
##print(week)
##
##week.discard("tuesday")
##print(week)
##
##week.remove("sat")
##print(week)
##
####week.remove("sunday")
####print(week)
##
##week.pop()
##print(week)
##
##y = week.pop()
##print(y)
##print(week)












































































































