userinfo = ["james",20,"male","from medina, misamis oriental"]

user = input(do you want to sort ur info or reverse?)
             
if user == "sort" :
   userinfo.sort()
   print(userinfo)
elif user == "reverse" :
   userinfo.reverse()
   print(userinfo)
else :
    print("your answer is not in the choices")   