##trainscanceled = [7 , 31 , 66 , 45 , 79 ,20]
##x = int(input("enter train number "))
##def mytrain(a,b):
##    
##    if b in a :
##        print(" your train has been canceled ")
##    elif b not in  a :
##        print(" your train has not been canceled ")
##mytrain(trainscanceled,x)



##giventuple = ("delhi" , "mumbai" , "goa" , "gujarat" , "rajasthan" , "jammu")
##a = input("enter city 1 name ")
##b = input("enter city 2 name ")
##def myflight(x,y,z):
##    if y in x and z in x:
##        print("your flight is a connecting flight ")
##    elif y in x and z not in x:
##        print("your flight is not a connecting flight ")
##    elif y not in x and z not in x:
##        print("your flight is not a connecting flight ")
##    else:
##        print("your flight is not a connecting flight ")
##myflight(giventuple,a,b)

        

##sciences = ["physics" , "chemistry" , "maths", "biology"]
##arts = ["political science" , "geaography" , "history" , "psychology"]
##commerce = ["accounts" , "business studies" , "finance"]
##sub = input("enter your subject ")
##
##def mysubject(s,a,c,d):
##    
##    if d in s:
##        print("you have been alloted the science stream ")
##    elif d in a:
##        print("you have been alloted the arts stream ")
##    elif d in c:
##        print("you have been alloted the commerce stream ")
##    else:
##        print("your subject not taught in school ")
##
##mysubject(sciences,arts,commerce,sub)
##    




##submarks = {"maths":26 , "physics":32 , "chemistry":34 , "english":38}
##def mymarks(s):
##    for i in s:
##        print(s[i])
##mymarks(submarks)












##capitalnames = {"india":"delhi" , "bangladesh":"dhaka" , "pakistan":"lahore" , "austrailia":"canberra" , "canada":"ottawa"}
##a = input("enter name of country ")
##def mycountryname(x,y):
##    if y == "india":
##        print(x[y])
##    elif y=="bangladesh":
##        print(x[y])
##    elif y=="pakistan":
##        print(x[y])
##    elif y=="austrailia":
##        print(x[y])
##    elif y =="canada":
##        print(x[y])
##mycountryname(capitalnames,a)
                




names = ["rohan" , "ajay" , "ganesh" , "manav" , "aryan"]
marks = [13 , 17 , 30 , 26 , 28]
def mylist(x,y):
    i = 0
    while  i <= 4:
        print(x[i] , "scored" , y[i] , "in maths ")        
        i = i + 1
mylist(names,marks)






































































































































